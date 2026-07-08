from unittest import result

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database import Base, engine
from backend.dependencies import get_db
from backend import models

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

from backend.security.exceptions import (
    validation_exception_handler,
    prompt_exception_handler,
    code_exception_handler,
    generic_exception_handler,
)

Base.metadata.create_all(bind=engine)


app = FastAPI()

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
    Exception,
    generic_exception_handler,
)



@app.get("/")
def home():
    return {
        "message": "PortfolioGPT Backend Running 🚀"
    }


@app.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    return {
        "status": "Database Connected"
    }


@app.get("/faq/search")
def faq_search(
    question: str,
    db: Session = Depends(get_db)
):

    # Security Layer


    question = validate_question(question)

    detect_prompt_injection(question)

    detect_malicious_request(question)



    result = search_faq(db, question)

    if result:
        return {
            "markdown": result.answer
        }


    answer = rag_pipeline(question)

    answer = sanitize_output(answer)

    return {
        "markdown": answer
    }