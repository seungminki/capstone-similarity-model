from fastapi import FastAPI
from app.routers import similarity, hatespeech, classification

description = """
CAPSTONE-2025 API helps you do awesome stuff. 🚀

1. content-similarity (cs)
2. hate-speech-detection (hd)
3. topic-classification (tc)

"""

app = FastAPI(
    title="Capstone-2025",
    description=description,
    summary="에브리타임 자동화 시스템 API",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(similarity.router)
app.include_router(hatespeech.router)
app.include_router(classification.router)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.post("/search/")
# def search(request: SearchRequest):
#     return client_query(request)
