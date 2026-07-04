from fastapi import FastAPI

from backend.database import Base, engine

from backend import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "PortfolioGPT Backend Running 🚀"}
