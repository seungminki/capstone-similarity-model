from fastapi import APIRouter
from app.schemas.post import PostRequest

router = APIRouter(prefix="/classification", tags=["classification"])


@router.get("/")
def get_tagging_list(req: PostRequest):
    # tag 검색
    # tag list 생성
    tag_list = []

    return {
        "created_user_id": req.user_id,
        "tag_list": tag_list,
    }
