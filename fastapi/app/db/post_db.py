import mysql.connector

from app.db.connection import get_rdbms_connection
from app.schemas.post import PostRequest


def insert_post(req: PostRequest):
    query = _create_insert_query()
    conn = get_rdbms_connection()
    cursor = conn.cursor(prepared=True)

    data = {
        "post_id": req.post_id,
        "board_id": req.board_id,
        "content": req.content,
        "user_id": req.user_id,
    }

    try:
        cursor.execute(query, data)
        conn.commit()
        print("✅ 게시글 삽입 성공")
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"❌ 삽입 실패: {e}")
    finally:
        cursor.close()
        conn.close()


def _create_insert_query():
    return """
    INSERT INTO posts (post_id, board_id, content, user_id)
    VALUES (%(post_id)s, %(board_id)s, %(content)s, %(user_id)s)
    """
