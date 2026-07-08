# Projects

## Insight Analyst – AI-Powered Data Analysis Agent

**Technologies:** Python, FastAPI, Streamlit, Pandas, Plotly, OpenAI API

- Built an AI-powered platform that automatically cleans, analyzes, and visualizes uploaded datasets containing 10,000+ records.
- Implemented automated data cleaning and natural language querying to generate insights and interactive dashboards.

---

## AWS Fraud Detection Pipeline

**Technologies:** AWS (S3, Lambda, DynamoDB), Python

- Designed and implemented a serverless ETL pipeline on AWS (S3, Lambda, DynamoDB) to ingest, transform, and store 500+ transaction records for fraud analytics.
- Automated ingestion using AWS Lambda, reducing manual effort by 40% and improving anomaly detection.

---

## CareerPrep AI – RAG Interview Chatbot

**Technologies:** Python, LangChain, Streamlit, Gemini API, RAG

- Built a RAG-based chatbot that helps users prepare for interviews using resumes, notes, and study materials.
- Implemented document ingestion, vector search, and LLM-powered Q&A for contextual interview preparation.

AI First Aid Assistant
## Overview
An AI-powered healthcare assistant providing first-aid guidance using Google's Gemini model.
Supports text and image inputs for symptom analysis.
## Architecture
User → Flask → Validation → Text/Image Processing → Gemini 1.5 Flash → Recommendation →
Web UI
## Tech Stack
Python, Flask, Google Gemini 1.5 Flash, Google Generative AI SDK, HTML, CSS, JavaScript,
dotenv.
## Features
Text and image-based first aid, multimodal AI, secure API handling, responsive UI.
## Skills Demonstrated
Flask, Prompt Engineering, Multimodal AI, REST APIs, Image Processing.
AI Job Agent
## Overview
An autonomous AI agent that searches jobs, parses resumes, computes semantic similarity,
verifies fresher roles with LLMs, and sends Telegram alerts.
## Architecture
Scheduler → Job APIs → Resume Parser → Embeddings → Cosine Similarity → Gemini/Groq
## Evaluation → Telegram.
## Tech Stack
Python, APScheduler, SentenceTransformers, Gemini, Groq Llama, PyPDF, Pandas, Telegram Bot
## API.
## Features
Automated job search, resume matching, semantic search, duplicate filtering, Telegram
notifications.
AI Techniques
Embeddings, Semantic Search, Cosine Similarity, Prompt Engineering, Resume Parsing.
## Revision Bot
## Overview
A LeetCode revision assistant that imports solved questions, stores them in SQLite, and generates
daily revision schedules through Streamlit.
## Architecture
LeetCode → Importer → SQLite → Difficulty Analysis → Revision Selector → Streamlit Dashboard.
## Tech Stack
Python, Streamlit, SQLite, SQLAlchemy, Pandas, Requests.
## Features

Daily revision generation, progress tracking, question categorization, dashboard.
## Skills Demonstrated
Automation, SQLAlchemy, Streamlit, Data Management.
Sameer.AI (PortfolioGPT)
## Overview
A conversational portfolio chatbot using a hybrid Retrieval-Augmented Generation pipeline with
PostgreSQL FAQ search and FAISS retrieval powered by Amazon Bedrock.
## Architecture
User → Streamlit → FastAPI → PostgreSQL (pg_trgm) → FAISS → Titan Embeddings → Claude
## Haiku → Response.
## Tech Stack
FastAPI, Streamlit, PostgreSQL, SQLAlchemy, FAISS, Docker, AWS Bedrock, Amazon Titan
## Embeddings, Claude Haiku.
## Features
Hybrid search, semantic retrieval, FAQ cache, RAG pipeline, markdown knowledge base.
## Skills Demonstrated
RAG, FastAPI, Docker, AWS Bedrock, Semantic Search, Hybrid Retrieval.