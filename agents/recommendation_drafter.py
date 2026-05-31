"""
ADK Agent — RecommendationDrafter

Synthesizes extracted compliance rules and gathered evidence into a
structured compliance recommendation.
"""
from google.adk.agents import LlmAgent


recommendation_drafter = LlmAgent(
    name="recommendation_drafter",
    model="gemini-2.5-flash",
    description=(
        "Drafts a structured compliance recommendation by synthesizing extracted "
        "regulation rules and gathered organizational evidence."
    ),
    instruction=(
        "You are a compliance recommendation drafter. You receive:\n"
        "1. PARSED RULES — structured compliance requirements from the applicable regulation\n"
        "2. EVIDENCE — current state of the organization relevant to those requirements\n"
        "3. THE REQUEST — the specific compliance question to answer\n\n"
        "Produce a structured recommendation with:\n"
        "- STATUS: Compliant / Non-Compliant / Needs Review\n"
        "- SUMMARY: 2-3 sentence plain-language summary\n"
        "- KEY FINDINGS: Bulleted list of specific compliance gaps or confirmations\n"
        "- ACTION ITEMS: Prioritized list (P1/P2/P3) of remediation steps with owners and timelines\n"
        "- CONFIDENCE: Your confidence in this recommendation (High/Medium/Low) and why\n\n"
        "Be conservative: if evidence is incomplete or ambiguous, rate as 'Needs Review' "
        "and flag the specific gap. Do not extrapolate beyond what the evidence supports."
    ),
    tools=[],
)