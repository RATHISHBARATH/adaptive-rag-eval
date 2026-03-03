from pydantic import BaseModel, Field
from typing import List

class AssessmentQuery(BaseModel):
    query: str = Field(..., description="Job description or skill query")

class AssessmentItem(BaseModel):
    url: str = Field(..., description="Valid URL to the assessment resource")
    name: str = Field(..., description="Name of the assessment")
    adaptive_support: str = Field(..., description="Either 'Yes' or 'No'")
    description: str = Field(..., description="Detailed description of the assessment")
    duration: int = Field(..., description="Duration of the assessment in minutes")
    remote_support: str = Field(..., description="Either 'Yes' or 'No'")
    test_type: List[str] = Field(..., description="Categories of the assessment")

class RecommendationResponse(BaseModel):
    recommended_assessments: List[AssessmentItem]