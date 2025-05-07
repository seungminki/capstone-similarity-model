import pandas as pd

from preprocess import load_and_preprocess
from utils.vector_db_util import get_collection, store_embeddings

# db get conntection
collection_client = get_collection()

# load_data
df = load_and_preprocess()

# preprocess for vector db form
df["id"] = df.index.map(lambda x: f"doc_{x}")

df = df.rename(columns={"post_code": "post_id"})
df = df.rename(columns={"board_code": "board_id"})

# save_to_vector_db
store_embeddings(collection_client=collection_client, df=df)

# status check!
