import os
import requests
from typing import Optional

from .schemas import ReasoningResponse


def cortexiom_reason(
    decision_point: str,
    context: str,
    state_token: Optional[str] = None,
) -> ReasoningResponse:
    """
    Call the Cortexiom API for a single reasoning checkpoint.

    decision_point: label for this checkpoint (e.g. 'pre_decision', 'post_recommendation', 'escalation')
    context:        structured summary of the workflow state at this point
    state_token:    opaque token from a prior call; enables multi-step session continuity
    """
    api_key = os.environ.get("CORTEXIOM_API_KEY", "")
    api_url = os.environ.get(
        "CORTEXIOM_API_URL", "https://api.cortexiom.com/v1/encounter"
    )

    if not api_key:
        raise ValueError(
            "CORTEXIOM_API_KEY is not set. "
            "Get your key at developers.cortexiom.com and add it to .env"
        )

    message = (
        f"[COMPLIANCE WORKFLOW — {decision_point.upper()}]\n\n"
        f"{context}\n\n"
        "Apply Wisdom Architecture reasoning: identify contradictions between "
        "the evidence and the regulation, flag confidence calibration gaps, "
        "surface any evidence that was not retrieved but should have been, "
        "and assess whether the current recommendation is adequately supported. "
        "Return a structured assessment with: (1) confidence in the current evidence "
        "chain, (2) any contradictions or gaps detected, (3) recommended action."
    )

    payload: dict = {
        "message": message,
        "persona": {
            "name": "Compliance Supervisor",
            "role": "Senior Compliance Analyst",
            "domain": "Regulatory Compliance and Risk Management",
        },
    }
    if state_token:
        payload["state_token"] = state_token

    resp = requests.post(
        api_url,
        json=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        timeout=180,
    )
    resp.raise_for_status()
    data = resp.json()

    return ReasoningResponse(
        response=data.get("response", ""),
        confidence=float(data.get("confidence", 0.5)),
        depth=int(data.get("depth", 0)),
        credits_used=int(data.get("credits_used", 1)),
        state_token=data.get("state_token"),
        reasoning_trace=data.get("response", ""),
    )