"""
Supervised workflow — compliance pipeline WITH Cortexiom at three checkpoints.

Checkpoint 1 — pre_decision:
    After evidence is gathered, before the recommendation is drafted.
    Cortexiom checks: evidence completeness, potential missing sources,
    confidence calibration. Its findings are injected into the drafter prompt.

Checkpoint 2 — post_recommendation:
    After the recommendation is drafted.
    Cortexiom checks: contradictions between the recommendation and the rules,
    overconfidence, and jurisdiction-specific edge cases the drafter may have missed.
    If a contradiction is found, the recommendation is revised.

Checkpoint 3 — escalation:
    Final routing decision.
    Cortexiom determines: file report / escalate to human / urgent review needed.
    State token carries reasoning continuity from all three calls.
"""
import os
from pathlib import Path
from typing import Any, Optional

from google import genai

from cortexiom import cortexiom_reason

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
KB_DIR = DATA_DIR / "knowledge_base"
REG_DIR = DATA_DIR / "regulations"

# Surface path problems immediately rather than silently returning no results
if not KB_DIR.exists():
    raise RuntimeError(
        f"Knowledge base directory not found: {KB_DIR}\n"
        f"Run streamlit from the cortexiom-orchestrator project root."
    )


def _make_client() -> genai.Client:
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY", "")
    if api_key:
        return genai.Client(api_key=api_key)
    return genai.Client(
        vertexai=True,
        project=os.environ.get("GCP_PROJECT_ID", "cortexiom-orchestrator"),
        location=os.environ.get("GCP_REGION", "us-central1"),
    )


def _generate(client: genai.Client, prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


def _load_regulation(file_name: str) -> str:
    path = REG_DIR / file_name
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"[Regulation file not found: {file_name}]"


def _search_knowledge_base(topic: str) -> str:
    keywords = [w.lower() for w in topic.split() if len(w) >= 3]
    results = []
    for doc_path in sorted(KB_DIR.glob("*.md")):
        content = doc_path.read_text(encoding="utf-8")
        if any(kw in content.lower() for kw in keywords):
            results.append(f"=== {doc_path.name} ===\n{content}")
    return "\n\n".join(results) if results else "No relevant documents found."


def run_supervised(test_case: dict[str, Any]) -> dict[str, Any]:
    """
    Run the compliance workflow with Cortexiom supervision at 3 checkpoints.

    The state_token is held in memory as a local variable and passed between
    each Cortexiom call, enabling multi-step reasoning continuity without
    any server-side state storage.

    Args:
        test_case: same structure as run_baseline

    Returns:
        dict with: parsed_rules, evidence, recommendation, final_recommendation,
                   cortexiom_checkpoints (list of dicts), error
    """
    state_token: Optional[str] = None
    checkpoints = []

    try:
        client = _make_client()

        # Stage 1 — DocumentParser (same as baseline)
        regulation_text = _load_regulation(test_case["regulation"])
        parse_prompt = (
            f"You are a compliance document parser. Extract all compliance rules.\n\n"
            f"REGULATION:\n{regulation_text}\n\n"
            f"Extract: applicable entities, mandatory requirements, thresholds, "
            f"effective dates, documentation standards, penalties."
        )
        parsed_rules = _generate(client, parse_prompt)

        # Stage 2 — EvidenceGatherer (same as baseline — knowledge_base/ only)
        evidence_text = _search_knowledge_base(test_case["topic"])
        gather_prompt = (
            f"You are a compliance evidence gatherer.\n\n"
            f"REQUEST: {test_case['request']}\n\n"
            f"DOCUMENTS:\n{evidence_text}\n\n"
            f"Summarize: current state, compliance gaps, missing information noted in documents."
        )
        evidence = _generate(client, gather_prompt)

        # ── CORTEXIOM CHECKPOINT 1 — pre_decision ──────────────────────────────
        checkpoint1_context = (
            f"CASE: {test_case['description']}\n\n"
            f"REQUEST: {test_case['request']}\n\n"
            f"REGULATION RULES EXTRACTED:\n{parsed_rules[:1200]}\n\n"
            f"EVIDENCE GATHERED (from knowledge_base/ only):\n{evidence[:1200]}\n\n"
            f"The workflow is about to draft a compliance recommendation based on "
            f"the above evidence. Before proceeding:\n"
            f"1. Assess whether the evidence gathered is complete for this regulation\n"
            f"2. Identify any evidence sources that should exist but were not retrieved\n"
            f"3. Flag any structural gaps (e.g. records that show completion dates "
            f"   but lack component-level detail required by the regulation)\n"
            f"4. Report confidence in proceeding with only this evidence"
        )
        cp1 = cortexiom_reason("pre_decision", checkpoint1_context)
        state_token = cp1.state_token
        checkpoints.append({
            "name": "Checkpoint 1 — Pre-Decision",
            "description": "Evidence completeness review before recommendation is drafted",
            "response": cp1.response,
            "confidence": cp1.confidence,
            "depth": cp1.depth,
            "state_token_received": bool(state_token),
        })

        # Stage 3 — RecommendationDrafter (enhanced with Cortexiom cp1 findings)
        draft_prompt = (
            f"You are a compliance recommendation drafter.\n\n"
            f"REQUEST: {test_case['request']}\n\n"
            f"APPLICABLE RULES:\n{parsed_rules}\n\n"
            f"EVIDENCE:\n{evidence}\n\n"
            f"CORTEXIOM PRE-DECISION ASSESSMENT:\n{cp1.response}\n\n"
            f"Take the Cortexiom assessment seriously — if it flags evidence gaps "
            f"or missing sources, reflect that uncertainty in your recommendation.\n\n"
            f"Structure:\n"
            f"- STATUS: Compliant / Non-Compliant / Needs Review\n"
            f"- SUMMARY: 2-3 sentence plain-language summary\n"
            f"- KEY FINDINGS: Specific compliance gaps\n"
            f"- CORTEXIOM FLAGS: Issues surfaced by the pre-decision assessment\n"
            f"- ACTION ITEMS: Prioritized (P1/P2/P3) with owners and timelines\n"
            f"- CONFIDENCE: High/Medium/Low and why"
        )
        recommendation = _generate(client, draft_prompt)

        # ── CORTEXIOM CHECKPOINT 2 — post_recommendation ───────────────────────
        checkpoint2_context = (
            f"CASE: {test_case['description']}\n\n"
            f"REGULATION RULES:\n{parsed_rules[:800]}\n\n"
            f"DRAFT RECOMMENDATION:\n{recommendation[:1500]}\n\n"
            f"Review this recommendation for:\n"
            f"1. Contradictions between the recommendation and the regulation rules\n"
            f"2. Jurisdiction-specific requirements that may have been missed\n"
            f"3. Any temporal issues (outdated evidence, pre/post regulatory change)\n"
            f"4. Whether the confidence level stated is calibrated to the evidence quality\n"
            f"5. Anything that would change the recommendation if true"
        )
        cp2 = cortexiom_reason("post_recommendation", checkpoint2_context, state_token)
        state_token = cp2.state_token or state_token
        checkpoints.append({
            "name": "Checkpoint 2 — Post-Recommendation",
            "description": "Contradiction detection and confidence calibration",
            "response": cp2.response,
            "confidence": cp2.confidence,
            "depth": cp2.depth,
            "state_token_received": bool(state_token),
        })

        # Revise recommendation based on Cortexiom cp2 findings
        revise_prompt = (
            f"You are a compliance recommendation drafter performing a revision.\n\n"
            f"ORIGINAL RECOMMENDATION:\n{recommendation}\n\n"
            f"CORTEXIOM POST-RECOMMENDATION REVIEW:\n{cp2.response}\n\n"
            f"Revise the recommendation to address the issues Cortexiom identified. "
            f"If contradictions or temporal gaps were found, update STATUS and CONFIDENCE "
            f"accordingly. Add a REVISION NOTES section explaining what changed and why."
        )
        final_recommendation = _generate(client, revise_prompt)

        # ── CORTEXIOM CHECKPOINT 3 — escalation ────────────────────────────────
        checkpoint3_context = (
            f"CASE: {test_case['description']}\n\n"
            f"FINAL RECOMMENDATION (after revision):\n{final_recommendation[:1500]}\n\n"
            f"Based on the full reasoning chain so far (pre-decision + post-recommendation), "
            f"determine the appropriate escalation routing:\n"
            f"1. FILE REPORT — documented and filed; no immediate escalation\n"
            f"2. HUMAN REVIEW — requires senior compliance officer review before action\n"
            f"3. URGENT ESCALATION — requires immediate action (CCO, legal, or regulator)\n\n"
            f"Provide the routing decision with rationale and any time-sensitive actions."
        )
        cp3 = cortexiom_reason("escalation", checkpoint3_context, state_token)
        state_token = cp3.state_token or state_token
        checkpoints.append({
            "name": "Checkpoint 3 — Escalation",
            "description": "Final routing: file / human review / urgent escalation",
            "response": cp3.response,
            "confidence": cp3.confidence,
            "depth": cp3.depth,
            "state_token_received": bool(state_token),
        })

        return {
            "parsed_rules": parsed_rules,
            "evidence": evidence,
            "recommendation": recommendation,
            "final_recommendation": final_recommendation,
            "cortexiom_checkpoints": checkpoints,
            "error": None,
        }

    except Exception as exc:
        err = str(exc)
        if any(s in err for s in ("Bearer", "cx_live", "api_key", "Authorization")):
            err = "API authentication error — check that CORTEXIOM_API_KEY is set correctly in the environment."
        return {
            "parsed_rules": "",
            "evidence": "",
            "recommendation": "",
            "final_recommendation": "",
            "cortexiom_checkpoints": checkpoints,
            "error": err,
        }
