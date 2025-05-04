from config import get_collection
import pandas as pd


def add_data_to_db():
    collection = get_collection()

    df = pd.read_json("", lines=True)
    df["id"] = df.index.map(lambda x: f"doc_{x}")

    df = df.rename(columns={"post_code": "post_id"})
    df = df.rename(columns={"board_code": "board_id"})

    def _batch_add_to_chroma(collection, ids, documents, metadatas, batch_size=10000):
        for i in range(0, len(ids), batch_size):
            collection.add(
                ids=ids[i : i + batch_size],
                documents=documents[i : i + batch_size],
                metadatas=metadatas[i : i + batch_size],
            )

    _batch_add_to_chroma(
        collection,
        ids=df["id"].tolist(),
        documents=df["text"].tolist(),
        metadatas=df[["post_id", "board_id"]].to_dict(orient="records"),
    )


def test_result(query: str):
    def _query_db(query):
        collection = get_collection()
        result = collection.query(
            query_texts=[query],
            n_results=10,
            include=[
                "documents",
                "distances",
            ],
        )

        return result

    result = _query_db(query)

    print("Query:", query)
    print("Most similar sentences:")

    ids = result.get("ids")[0]
    documents = result.get("documents")[0]
    distances = result.get("distances")[0]

    for id_, document, distance in zip(ids, documents, distances):
        print(f"ID: {id_}, Document: {document}, Similarity: {1 - distance}")


if __name__ == "__main__":
    query = "학생식당 위치가 어디에 있는거임?"
    test_result(query)
