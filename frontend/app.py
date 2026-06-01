"""
Cortexiom Orchestrator — Streamlit Demo

Side-by-side comparison: baseline multi-agent workflow vs. Cortexiom-supervised workflow.
Demonstrates how Cortexiom catches what baseline misses at three reasoning checkpoints.

Run:
    streamlit run frontend/app.py
"""
import sys
import time
from pathlib import Path

import streamlit as st

# Allow imports from project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

load_dotenv()

from test_cases import TEST_CASES
from workflow import run_baseline, run_supervised


def md(text: str) -> None:
    """Render workflow output as markdown, escaping $ to prevent LaTeX rendering."""
    st.markdown(text.replace("$", r"\$") if text else "—")

# ─── Page config ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Cortexiom Orchestrator Demo",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Styles ──────────────────────────────────────────────────────────────────

st.markdown(
    """
    <style>
    .main { background-color: #0a0e18; color: #e2e8f0; }
    .block-container { padding-top: 2rem; }

    .cortexiom-header {
        background: linear-gradient(135deg, #1a3a8f 0%, #0f1f5c 100%);
        border-radius: 8px;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid #2a4aaf;
    }
    .checkpoint-card {
        background: #0f1420;
        border: 1px solid #1a3a8f;
        border-left: 4px solid #4f75ff;
        border-radius: 6px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
    }
    .checkpoint-meta {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        font-family: monospace;
    }
    .confidence-high { color: #4ade80; }
    .confidence-medium { color: #facc15; }
    .confidence-low { color: #f87171; }
    .baseline-col { border-right: 1px solid #1e2a40; }
    .status-badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── Sidebar ─────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🧠 Cortexiom Orchestrator")
    st.caption("Google for Startups AI Agents Challenge — 2026")
    st.divider()

    st.markdown("### Select Test Case")
    case_options = {tc["title"]: tc for tc in TEST_CASES}
    selected_title = st.selectbox(
        "Compliance scenario",
        options=list(case_options.keys()),
        label_visibility="collapsed",
    )
    test_case = case_options[selected_title]

    st.markdown("---")
    st.markdown(f"**Scenario:** {test_case['description']}")
    st.markdown(f"**Regulation:** `{test_case['regulation']}`")
    st.markdown("---")

    run_btn = st.button("▶ Run Comparison", use_container_width=True, type="primary")

    st.markdown("---")
    st.caption(
        "Cortexiom API adds three reasoning checkpoints:\n\n"
        "**CP1** — Evidence completeness\n\n"
        "**CP2** — Contradiction detection\n\n"
        "**CP3** — Escalation routing"
    )
    st.caption("Built on Google ADK 2.0 + Gemini 2.5 Flash")

# ─── Header ──────────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="cortexiom-header">
        <h2 style="margin:0;color:#e2e8f0;">Compliance Workflow — Baseline vs. Supervised</h2>
        <p style="margin:0.4rem 0 0;color:#94a3b8;font-size:0.9rem;">
            Watch Cortexiom catch what a standard multi-agent pipeline misses.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Request display ─────────────────────────────────────────────────────────

st.markdown(f"**Request:** {test_case['request']}")
st.markdown("---")

# ─── Run ─────────────────────────────────────────────────────────────────────

if run_btn:
    col_base, col_sup = st.columns(2)

    with col_base:
        st.markdown("### 🔵 Baseline Workflow")
        st.caption("DocumentParser → EvidenceGatherer → RecommendationDrafter")
        with st.spinner("Running baseline workflow…"):
            t0 = time.time()
            baseline_result = run_baseline(test_case)
            base_elapsed = time.time() - t0

    with col_sup:
        st.markdown("### 🟣 Supervised Workflow (+ Cortexiom)")
        st.caption(
            "DocumentParser → EvidenceGatherer → **Cortexiom CP1** → "
            "RecommendationDrafter → **Cortexiom CP2** → Revision → **Cortexiom CP3**"
        )
        with st.spinner("Running supervised workflow — 3 Cortexiom checkpoints (5-layer reasoning pipeline each, ~2–3 min total)…"):
            t0 = time.time()
            supervised_result = run_supervised(test_case)
            sup_elapsed = time.time() - t0

    # ── Error handling ────────────────────────────────────────────────────────

    if baseline_result.get("error"):
        col_base.error(f"Baseline error: {baseline_result['error']}")
    if supervised_result.get("error"):
        col_sup.error(f"Supervised error: {supervised_result['error']}")

    st.markdown("---")

    # ── Stage comparison ──────────────────────────────────────────────────────

    st.markdown("## Results")
    col_base, col_sup = st.columns(2)

    with col_base:
        st.markdown(f"**Elapsed:** {base_elapsed:.1f}s")
        with st.expander("📋 Parsed Regulation Rules", expanded=False):
            md(baseline_result.get("parsed_rules", "—"))

        with st.expander("🔍 Evidence Gathered", expanded=False):
            md(baseline_result.get("evidence", "—"))

        st.markdown("### Final Recommendation")
        md(baseline_result.get("recommendation", "—"))

    with col_sup:
        st.markdown(f"**Elapsed:** {sup_elapsed:.1f}s")
        with st.expander("📋 Parsed Regulation Rules", expanded=False):
            md(supervised_result.get("parsed_rules", "—"))

        with st.expander("🔍 Evidence Gathered", expanded=False):
            md(supervised_result.get("evidence", "—"))

        # ── Cortexiom checkpoints ─────────────────────────────────────────────
        checkpoints = supervised_result.get("cortexiom_checkpoints", [])
        if checkpoints:
            st.markdown("### 🧠 Cortexiom Reasoning Checkpoints")
            for cp in checkpoints:
                confidence = cp.get("confidence", 0.5)
                conf_pct = int(confidence * 100)
                if confidence >= 0.75:
                    conf_class = "confidence-high"
                    conf_icon = "🟢"
                elif confidence >= 0.5:
                    conf_class = "confidence-medium"
                    conf_icon = "🟡"
                else:
                    conf_class = "confidence-low"
                    conf_icon = "🔴"

                with st.expander(
                    f"**{cp['name']}** — Confidence {conf_icon} {conf_pct}%",
                    expanded=True,
                ):
                    st.caption(cp.get("description", ""))
                    st.markdown(
                        f"<div class='checkpoint-meta'>"
                        f"depth={cp.get('depth', 0)} | "
                        f"state_token={'✓ active' if cp.get('state_token_received') else '—'}"
                        f"</div>",
                        unsafe_allow_html=True,
                    )
                    md(cp.get("response", "—"))

        st.markdown("### Final Recommendation (Cortexiom-Revised)")
        final = supervised_result.get("final_recommendation") or supervised_result.get("recommendation", "—")
        md(final)

    # ── What Cortexiom caught ─────────────────────────────────────────────────

    st.markdown("---")
    st.markdown("## What Cortexiom caught")

    col_expected, col_actual = st.columns(2)
    with col_expected:
        st.markdown("**Expected baseline flaw:**")
        st.info(test_case.get("expected_baseline_flaw", ""))
    with col_actual:
        st.markdown("**Expected Cortexiom intervention:**")
        st.success(test_case.get("expected_cortexiom_catch", ""))

else:
    # ── Intro state ───────────────────────────────────────────────────────────
    st.markdown(
        """
        ### How this demo works

        Select a compliance scenario from the sidebar and click **▶ Run Comparison**.

        The demo runs two versions of the same multi-agent pipeline:

        | | Baseline | Supervised |
        |---|---|---|
        | DocumentParser | ✅ | ✅ |
        | EvidenceGatherer | ✅ | ✅ |
        | **Cortexiom CP1 (pre-decision)** | ❌ | ✅ |
        | RecommendationDrafter | ✅ | ✅ (informed by CP1) |
        | **Cortexiom CP2 (post-recommendation)** | ❌ | ✅ |
        | Recommendation Revision | ❌ | ✅ |
        | **Cortexiom CP3 (escalation routing)** | ❌ | ✅ |

        Each test case has a structural flaw that the baseline misses — a piece of
        evidence outside the search scope, a temporal gap in legal opinions, a
        jurisdiction-specific rule, or a critical timeline conflict. Cortexiom
        catches it at the appropriate checkpoint.
        """
    )

    st.markdown("---")
    st.markdown("### Test Cases")
    for tc in TEST_CASES:
        with st.expander(f"**{tc['title']}**"):
            st.markdown(f"**Scenario:** {tc['description']}")
            st.markdown(f"**Request:** {tc['request']}")
            col1, col2 = st.columns(2)
            with col1:
                st.error(f"**Baseline misses:** {tc['expected_baseline_flaw']}")
            with col2:
                st.success(f"**Cortexiom catches:** {tc['expected_cortexiom_catch']}")