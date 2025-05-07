import pandas as pd
import chromadb

from embedding_util import CustomEmbeddingFunction
from settings import collection_name, chroma_localhost, chroma_port


def store_embeddings(collection_client, df: pd.DataFrame):
    def _batch_add_to_chroma(collection, ids, documents, metadatas, batch_size=10000):
        for i in range(0, len(ids), batch_size):
            collection.add(
                ids=ids[i : i + batch_size],
                documents=documents[i : i + batch_size],
                metadatas=metadatas[i : i + batch_size],
            )

    _batch_add_to_chroma(
        collection_client,
        ids=df["id"].tolist(),
        documents=df["text"].tolist(),
        metadatas=df[["post_id", "board_id"]].to_dict(orient="records"),
    )


def get_collection():
    def _get_client():
        chroma_client = chromadb.HttpClient(host=chroma_localhost, port=chroma_port)
        return chroma_client

    client = _get_client()

    collection = client.get_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
        embedding_function=CustomEmbeddingFunction(),
    )  # l2 is the default

    return collection


if __name__ == "__main__":
    query = "학생식당 위치가 어디에 있는거임?"
