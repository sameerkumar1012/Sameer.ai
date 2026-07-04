from unittest import result
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import Base, engine
from backend.dependencies import get_db
from backend import models
from backend.faq_service import search_faq

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "PortfolioGPT Backend Running 🚀"}

@app.get("/health/db")
def db_health(db: Session = Depends(get_db)):
    return {"status": "Database Connected"}

@app.get("/faq/search")
def faq_search(question: str, db: Session = Depends(get_db)):

    result = search_faq(db, question)

    if result is None:
        return {
            "message": "No matching FAQ found. Proceed to RAG."
        }

    return {
    "markdown": result.answer
}