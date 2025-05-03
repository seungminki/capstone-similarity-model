from pydantic import BaseModel
from typing import Optional


class PostRequest(BaseModel):
    post_id: int
    board_id: int
    content: Optional[str] = None
    user_id: Optional[int] = None
    tag: Optional[int] = None
