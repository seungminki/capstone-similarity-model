from fastapi import APIRouter
from app.schemas.post import PostRequest

# from app.schemas.similarity import SimilarityRequest

import random

router = APIRouter(prefix="/hatespeech", tags=["hatespeech"])


@router.get("/")
def get_negative_score(req: PostRequest):

    negative_score = round(random.uniform(0, 1), 2)  # 측정

    return {
        "post_id": req.post_id,
        "board_id": req.board_id,
        "negative_score": negative_score,
    }
