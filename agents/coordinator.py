"""
ADK Agent — Coordinator (root agent for `adk run`)

Orchestrates the compliance workflow using sub-agents as tools.
This is the agent used when running via `adk run .` from the project root.
For the Streamlit demo, use workflow/supervised.py or workflow/baseline.py directly.
"""
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .document_parser import document_parser
from .evidence_gatherer import evidence_gatherer
from .recommendation_drafter import recommendation_drafter


coordinator = LlmAgent(
    name="coordinator",
    model="gemini-2.5-flash",
    description=(
        "Orchestrates a multi-agent compliance evaluation workflow: "
        "parses regulation, gathers evidence, then drafts a recommendation."
    ),
    instruction=(
        "You are a compliance workflow coordinator. When given a compliance request, "
        "execute the following pipeline in order:\n\n"
        "STEP 1 — Parse Regulation\n"
        "Call document_parser with the regulation filename relevant to the request. "
        "Ask it to extract all compliance rules.\n\n"
        "STEP 2 — Gather Evidence\n"
        "Call evidence_gatherer with the compliance topic. "
        "Ask it to retrieve all relevant internal documents and summarize current state.\n\n"
        "STEP 3 — Draft Recommendation\n"
        "Call recommendation_drafter with:\n"
        "  - The parsed rules from Step 1\n"
        "  - The evidence from Step 2\n"
        "  - The original compliance request\n"
        "Ask it to produce a structured compliance recommendation.\n\n"
        "STEP 4 — Present Result\n"
        "Return the full recommendation to the user, including:\n"
        "  - Status (Compliant / Non-Compliant / Needs Review)\n"
        "  - Key findings\n"
        "  - Action items with priorities\n"
        "  - Confidence level\n\n"
        "Regulation filenames available:\n"
        "  - edd_regulation.md (PEP enhanced due diligence)\n"
        "  - data_residency_policy.md (data residency requirements)\n"
        "  - hie_consent_regulation.md (health information exchange consent)\n"
        "  - advisor_conflict_disclosure.md (advisor conflict of interest disclosure)\n"
        "  - cross_border_data_transfer.md (cross-border data transfer rules)\n"
    ),
    tools=[
        AgentTool(agent=document_parser),
        AgentTool(agent=evidence_gatherer),
        AgentTool(agent=recommendation_drafter),
    ],
)