import chromadb
from embedding_util import CustomEmbeddingFunction

collection_name = ""
chroma_localhost = ""
chroma_port = 0


def get_client():
    chroma_client = chromadb.HttpClient(host=chroma_localhost, port=chroma_port)
    return chroma_client


def get_collection():
    client = get_client()

    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
        embedding_function=CustomEmbeddingFunction(),
    )  # l2 is the default

    return collection


def delete_collection(collection_name: str):
    client = get_client()
    return client.delete_collection(collection_name)


def list_collections():
    client = get_client()
    print(client.list_collections())


if __name__ == "__main__":
    get_collection()
    list_collections()
