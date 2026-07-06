from unittest import result
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.database import Base, engine
from backend.dependencies import get_db
from backend import models
from backend.faq_service import search_faq
from backend.rag_service import rag_pipeline

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

    if result:

        return {
            "markdown": result.answer
        }

    answer = rag_pipeline(question)

    return {
        "markdown": answer
    }