from fastapi import APIRouter

# from app.schemas.similarity import SimilarityRequest
from app.schemas.post import PostRequest
from app.db.post_db import insert_post
from app.db.vector_search import search_similar

router = APIRouter(prefix="/similarity", tags=["similarity"])


@router.get("/")
def get_similarity(req: PostRequest):

    # TODO: try-catch
    insert_post(req)

    documents = search_similar(req.content)

    return {
        # "post_id": req.post_id,
        # "board_id": req.board_id,
        "content": req.content,
        # "user_id": req.user_id,
        "documents": documents,
    }
