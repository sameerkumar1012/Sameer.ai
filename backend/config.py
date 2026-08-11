import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Repo root, so paths work no matter which directory uvicorn is started from.
BASE_DIR = Path(__file__).resolve().parent.parent

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

# Optional. Without it the FAQ cache is skipped and every question goes
# straight to RAG — slower and pricier, but the service still answers.
# Never hardcode a fallback here; it would end up in git history.

DATABASE_URL = os.getenv("DATABASE_URL")

# ------------------------
# Retrieval
# ------------------------

TOP_K = int(os.getenv("TOP_K", 3))

FAQ_THRESHOLD = float(os.getenv("FAQ_THRESHOLD", 0.4))

# ------------------------
# Vector Store
# ------------------------

VECTOR_INDEX = BASE_DIR / "vector.index"

METADATA_FILE = BASE_DIR / "metadata.pkl"

KNOWLEDGE_DIR = BASE_DIR / "knowledge"

# ------------------------
# Web access
# ------------------------

# Comma-separated list of browser origins allowed to call this API directly.
# The portfolio site proxies server-side and does not need to be listed.

ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]

# Optional. When set, callers must send it as the X-Portfolio-Secret header.

SHARED_SECRET = os.getenv("BACKEND_SHARED_SECRET")
