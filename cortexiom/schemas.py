from pydantic import BaseModel
from typing import Optional


class ReasoningRequest(BaseModel):
    decision_point: str
    context: str
    state_token: Optional[str] = None


class ReasoningResponse(BaseModel):
    response: str
    confidence: float
    depth: int
    credits_used: int
    state_token: Optional[str] = None
    reasoning_trace: str = ""