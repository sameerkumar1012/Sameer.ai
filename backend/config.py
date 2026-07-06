import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------
# AWS
# ------------------------

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

EMBEDDING_MODEL = "amazon.titan-embed-text-v2:0"

LLM_MODEL = "amazon.nova-lite-v1:0"

# ------------------------
# Retrieval
# ------------------------

TOP_K = 3

# ------------------------
# Vector Store
# ------------------------

VECTOR_INDEX = "vector.index"

METADATA_FILE = "metadata.pkl"