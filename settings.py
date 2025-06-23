import os
from dotenv import load_dotenv

load_dotenv()

AWS_S3_BUCKET_NAME = os.getenv("aws_s3_bucket_name")
AWS_S3_KEY_ID = os.getenv("aws_s3_id")
AWS_S3_SECRET_KEY = os.getenv("aws_s3_key")

CHROMA_COLLECTION_NAME = "capstone_0519"
CHROMA_HOST = os.getenv("chroma_host")
CHROMA_PORT = os.getenv("chroma_port")

ST_MODEL_NAME = "jhgan/ko-sroberta-multitask"

S3_FILE_PATH = "raw_output.json"
