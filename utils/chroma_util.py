import pandas as pd
import chromadb

from utils.embedding_util import CustomEmbeddingFunction


def store_embeddings(collection_client, df: pd.DataFrame):
    # new_df = filter_new_ids(collection_client, df)
    df.info()

    batch_add_to_chroma(
        collection_client,
        ids=df["id"].tolist(),
        documents=df["text"].tolist(),
        metadatas=df[["post_id", "board_id"]].to_dict(orient="records"),
        batch_size=500,
    )


def get_collection(collection_name, host, port):
    client = chromadb.HttpClient(host=host, port=port)

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
        embedding_function=CustomEmbeddingFunction(),
    )  # l2 is the default

    return collection


def filter_new_ids(collection, df):
    existing = collection.get(ids=df["id"].tolist())
    existing_ids = set(existing["ids"])
    return df[~df["id"].isin(existing_ids)].reset_index(drop=True)


def batch_add_to_chroma(collection, ids, documents, metadatas, batch_size=10000):
    for i in range(0, len(ids), batch_size):
        collection.add(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )
