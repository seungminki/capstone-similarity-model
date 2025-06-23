import pandas as pd

from preprocess import load_data, preprocess, generate_doc_ids
from utils.chroma_util import get_collection, store_embeddings

from settings import CHROMA_COLLECTION_NAME, CHROMA_HOST, CHROMA_PORT, S3_FILE_PATH

# load_data
df = load_data(S3_FILE_PATH)

# preprocess
df = preprocess(df)

# data for vector db form
# df["id"] = df.index.map(lambda x: f"doc_{x}")
df = generate_doc_ids(df)

# db get conntection
collection_client = get_collection(
    collection_name=CHROMA_COLLECTION_NAME, host=CHROMA_HOST, port=CHROMA_PORT
)

# save_to_vector_db
store_embeddings(collection_client=collection_client, df=df)

# status check!
