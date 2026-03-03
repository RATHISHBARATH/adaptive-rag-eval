from fastapi import APIRouter, HTTPException, Depends
from src.api.schemas import AssessmentQuery, RecommendationResponse
from src.rag.llm_client import SHLRecommender
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

engine = SHLRecommender()

def get_engine():
    return engine

@router.get("/health", status_code=200)
async def health_check():
    """Appendix 2: Health Check Endpoint"""
    return {"status": "healthy"}

@router.post("/recommend", response_model=RecommendationResponse, status_code=200)
async def recommend_assessments(
    payload: AssessmentQuery, 
    rag_engine: SHLRecommender = Depends(get_engine)
):
    """Appendix 2: Assessment Recommendation Endpoint"""
    try:
        results = await rag_engine.get_recommendation(payload.query)
        if not results.get("recommended_assessments"):
            raise HTTPException(status_code=404, detail="No relevant assessments found.")
        return results
    except Exception as e:
        logger.error(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))