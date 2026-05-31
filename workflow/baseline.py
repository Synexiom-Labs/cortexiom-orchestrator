"""
Baseline workflow — multi-agent compliance pipeline WITHOUT Cortexiom supervision.

Uses three Gemini calls directly:
  1. DocumentParser  — extract rules from regulation
  2. EvidenceGatherer — search knowledge_base/ only (not adverse_flags/)
  3. RecommendationDrafter — synthesize recommendation

Returns a dict with each stage's output and an empty cortexiom_checkpoints list.
"""
import os
from pathlib import Path
from typing import Any

from google import genai

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
    # Fall back to Vertex AI ADC
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
    return "\n\n".join(results) if results else "No relevant documents found in knowledge base."


def run_baseline(test_case: dict[str, Any]) -> dict[str, Any]:
    """
    Run the compliance workflow without Cortexiom supervision.

    Args:
        test_case: dict with keys:
            regulation (str): regulation filename
            request    (str): compliance question
            topic      (str): search keywords for evidence gathering
            description (str): human-readable scenario description

    Returns:
        dict with keys: parsed_rules, evidence, recommendation, cortexiom_checkpoints, error
    """
    try:
        client = _make_client()

        # Stage 1 — DocumentParser
        regulation_text = _load_regulation(test_case["regulation"])
        parse_prompt = (
            f"You are a compliance document parser. Extract all compliance rules from "
            f"this regulation document.\n\n"
            f"REGULATION:\n{regulation_text}\n\n"
            f"Extract and list:\n"
            f"1. Applicable entities\n"
            f"2. Mandatory requirements\n"
            f"3. Numeric thresholds\n"
            f"4. Effective dates and deadlines\n"
            f"5. Documentation standards\n"
            f"6. Penalties for non-compliance\n\n"
            f"Be precise. Do not soften mandatory language."
        )
        parsed_rules = _generate(client, parse_prompt)

        # Stage 2 — EvidenceGatherer (knowledge_base/ only — no adverse_flags/)
        evidence_text = _search_knowledge_base(test_case["topic"])
        gather_prompt = (
            f"You are a compliance evidence gatherer. Extract all compliance-relevant "
            f"facts for this request: {test_case['request']}\n\n"
            f"AVAILABLE DOCUMENTS:\n{evidence_text}\n\n"
            f"Summarize:\n"
            f"1. Current organizational state\n"
            f"2. Compliance gaps identified in the documents\n"
            f"3. Any missing information noted in the documents themselves\n\n"
            f"Report only what is in the documents. Do not speculate."
        )
        evidence = _generate(client, gather_prompt)

        # Stage 3 — RecommendationDrafter
        draft_prompt = (
            f"You are a compliance recommendation drafter.\n\n"
            f"REQUEST: {test_case['request']}\n\n"
            f"APPLICABLE RULES:\n{parsed_rules}\n\n"
            f"EVIDENCE:\n{evidence}\n\n"
            f"Produce a structured recommendation:\n"
            f"- STATUS: Compliant / Non-Compliant / Needs Review\n"
            f"- SUMMARY: 2-3 sentence plain-language summary\n"
            f"- KEY FINDINGS: Specific compliance gaps or confirmations\n"
            f"- ACTION ITEMS: Prioritized list (P1/P2/P3) with owners and timelines\n"
            f"- CONFIDENCE: High/Medium/Low and why\n\n"
            f"Be conservative. Flag ambiguity as 'Needs Review'."
        )
        recommendation = _generate(client, draft_prompt)

        return {
            "parsed_rules": parsed_rules,
            "evidence": evidence,
            "recommendation": recommendation,
            "cortexiom_checkpoints": [],
            "error": None,
        }

    except Exception as exc:
        return {
            "parsed_rules": "",
            "evidence": "",
            "recommendation": "",
            "cortexiom_checkpoints": [],
            "error": str(exc),
        }
