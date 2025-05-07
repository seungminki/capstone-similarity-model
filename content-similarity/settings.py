import os
from dotenv import load_dotenv

load_dotenv()

collection_name = ""
chroma_localhost = os.getenv("openai_token")
chroma_port = 8000
