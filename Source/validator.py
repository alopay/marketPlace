from pydantic import BaseModel, Field
from typing import List

class ListRequest(BaseModel):
    listing_name: str
    description: str
    features: dict[str, str] = Field(default_factory=dict)

class Issues(BaseModel):
    problem: str
    suggestion: str

class ValidationResponse(BaseModel):
    listing_name: str
    compliance_score: int
    issues: List[Issues] = Field(default_factory=list)