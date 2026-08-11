from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend import models  # noqa: F401  (registers tables on Base)
from backend.config import ALLOWED_ORIGINS, SHARED_SECRET
from backend.database import Base, db_enabled, engine
from backend.dependencies import get_db
from backend.logger import logger

from backend.faq_service import search_faq
from backend.rag_service import rag_pipeline

# Security Imports

from backend.security.validators import (
    validate_question,
    ValidationError,
)

from backend.security.prompt_guard import (
    detect_prompt_injection,
    PromptInjectionError,
)

from backend.security.code_guard import (
    detect_malicious_request,
    UnsafeCodeRequest,
)

from backend.security.output_guard import (
    sanitize_output,
)

from backend.security.budget import BudgetExceeded

from backend.security.exceptions import (
    validation_exception_handler,
    prompt_exception_handler,
    code_exception_handler,
    budget_exception_handler,
    generic_exception_handler,
)


# Table creation is best-effort: the FAQ cache is optional, so an unreachable
# database must not stop the service from booting.
if db_enabled():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as exc:
        logger.warning("Could not create FAQ tables: %s", exc)


app = FastAPI(title="Sameer.AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-Portfolio-Secret"],
)

app.add_exception_handler(
    ValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    PromptInjectionError,
    prompt_exception_handler,
)

app.add_exception_handler(
    UnsafeCodeRequest,
    code_exception_handler,
)

app.add_exception_handler(
    BudgetExceeded,
    budget_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)


# ----------------------------------------------------------------------
# Auth
# ----------------------------------------------------------------------

def require_secret(x_portfolio_secret: str | None = Header(default=None)):
    """
    Shared-secret check so only the portfolio site can drive the LLM.

    No-op when BACKEND_SHARED_SECRET is unset, which keeps local development
    and the Streamlit frontend working without extra configuration.
    """

    if SHARED_SECRET and x_portfolio_secret != SHARED_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized.")


# ----------------------------------------------------------------------
# Models
# ----------------------------------------------------------------------

class ChatRequest(BaseModel):
    question: str


# ----------------------------------------------------------------------
# Shared pipeline
# ----------------------------------------------------------------------

def answer_question(question: str, db: Session | None):
    """
    Runs the full guarded pipeline and returns (answer, sources).

    Order matters: cheap rejections first, then the free FAQ cache, and only
    then the paid embedding + generation path.
    """

    question = validate_question(question)

    detect_prompt_injection(question)

    detect_malicious_request(question)

    if db is not None:
        try:
            cached = search_faq(db, question)
            if cached:
                return sanitize_output(cached.answer), []
        except Exception as exc:
            # A broken cache should degrade to RAG, not fail the request.
            logger.warning("FAQ lookup failed, falling back to RAG: %s", exc)

    answer, chunks = rag_pipeline(question)

    sources = [
        {"source": chunk["source"], "title": chunk["title"]}
        for chunk in chunks
    ]

    return sanitize_output(answer), sources


# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "PortfolioGPT Backend Running 🚀"
    }


@app.get("/healthz")
def healthz():
    """Liveness probe. Must not depend on the database or on AWS."""

    return {
        "status": "ok",
        "faq_cache": "enabled" if db_enabled() else "disabled",
    }


@app.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    if db is None:
        return {"status": "Database Disabled"}

    return {
        "status": "Database Connected"
    }


@app.post("/chat", dependencies=[Depends(require_secret)])
def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
):
    """Primary endpoint for the portfolio site."""

    answer, sources = answer_question(payload.question, db)

    return {
        "answer": answer,
        "sources": sources,
    }


@app.get("/faq/search")
def faq_search(
    question: str,
    db: Session = Depends(get_db),
):
    """Kept for the Streamlit frontend, which expects `markdown`."""

    answer, _ = answer_question(question, db)

    return {
        "markdown": answer
    }
