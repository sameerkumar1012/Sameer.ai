import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------
# AWS
# ------------------------

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "amazon.titan-embed-text-v2:0"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "amazon.nova-lite-v1:0"
)

# ------------------------
# Database
# ------------------------

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:Sameer123@localhost:5432/portfolio_gpt"
)

# ------------------------
# Retrieval
# ------------------------

TOP_K = int(os.getenv("TOP_K", 3))

FAQ_THRESHOLD = float(os.getenv("FAQ_THRESHOLD", 0.65))

# ------------------------
# Vector Store
# ------------------------

VECTOR_INDEX = "vector.index"

METADATA_FILE = "metadata.pkl"