from fastapi import APIRouter, Depends, HTTPException
from ..ai_service import recommend_for_user

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/recommend/{user_id}")
async def recommend(user_id: int):
    recs = await recommend_for_user(user_id)
    return {"user_id": user_id, "recommendations": recs}
