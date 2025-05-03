from app.db.embedding_util import CustomEmbeddingFunction
from app.db.connection import get_vector_collection

collection_name = "jhgan_ko-sroberta-multitask_250503"


def search_similar(query_sentence):
    collection = _load_collection()
    result = collection.query(
        query_texts=[query_sentence],
        n_results=5,
        include=[
            "documents",
            "distances",
        ],
    )

    return _postprocess_results(result)


def _load_collection():
    chroma_client = get_vector_collection()

    collection = chroma_client.get_collection(
        name=collection_name,
        embedding_function=CustomEmbeddingFunction(),
    )

    return collection


def _postprocess_results(result):
    # print("Query:", ko_query)
    # print("Most similar sentences:")

    # ids = result.get("ids")[0]
    documents = result.get("documents")[0]
    # distances = result.get("distances")[0]

    # for id_, document, distance in zip(ids, documents, distances):
    #     print(f"ID: {id_}, Document: {document}, Similarity: {1 - distance}")

    return documents
