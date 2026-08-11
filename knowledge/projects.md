# Projects

## Sameer.AI (PortfolioGPT)

**Technologies:** FastAPI, Streamlit, PostgreSQL, SQLAlchemy, FAISS, Docker, AWS Bedrock, Amazon Titan Embeddings, Claude Haiku

A conversational portfolio chatbot using a hybrid Retrieval-Augmented Generation pipeline with a PostgreSQL FAQ cache and FAISS semantic retrieval powered by Amazon Bedrock.

- Architecture: User → FastAPI → security guards → PostgreSQL FAQ cache (pg_trgm) → FAISS + Titan embeddings → Bedrock LLM → sanitized response.
- Two-tier retrieval: common questions resolve from the FAQ cache without any LLM call; only novel questions pay for embedding and generation.
- Security layer covering prompt injection detection, malicious code request filtering, output sanitization and a daily cost budget.
- Answers are grounded strictly in retrieved context, with an explicit refusal when the corpus does not cover the question.
- Skills demonstrated: RAG, hybrid retrieval, semantic search, FastAPI, Docker, AWS Bedrock, prompt security.

---

## Calendar.AI (Meeting Scheduler)

**Technologies:** FastAPI, Google Calendar API, OAuth 2.0, Pydantic

A self-service meeting scheduler that reads and writes Sameer's real Google Calendar.

- Computes genuinely free slots by intersecting declared weekly availability with live free/busy data from the Google Calendar API.
- Creates a confirmed calendar event with a Google Meet link and emails the invite to the attendee.
- Re-validates the requested slot against live availability at booking time, so a stale page cannot double-book.
- Runs headless on a refresh token; the interactive OAuth consent flow is a local one-off script.
- Skills demonstrated: Google Calendar API, OAuth 2.0, FastAPI, timezone handling, API design.

---

## Insight Analyst – AI-Powered Data Analysis Agent

**Technologies:** Python, FastAPI, Streamlit, Pandas, Plotly, OpenAI API

- Built an AI-powered platform that automatically cleans, analyzes, and visualizes uploaded datasets containing 10,000+ records.
- Implemented automated data cleaning and natural language querying to generate insights and interactive dashboards.
- Skills demonstrated: data cleaning, LLM applications, data visualization.

---

## AWS Fraud Detection Pipeline

**Technologies:** AWS (S3, Lambda, DynamoDB), Python

- Designed and implemented a serverless ETL pipeline on AWS to ingest, transform, and store 500+ transaction records for fraud analytics.
- Automated ingestion using AWS Lambda, reducing manual effort by 40% and improving anomaly detection.
- Skills demonstrated: ETL pipelines, AWS Lambda, serverless architecture.

---

## CareerPrep AI – RAG Interview Chatbot

**Technologies:** Python, LangChain, Streamlit, Gemini API, RAG

- Built a RAG-based chatbot that helps users prepare for interviews using resumes, notes, and study materials.
- Implemented document ingestion, vector search, and LLM-powered Q&A for contextual interview preparation.
- Skills demonstrated: RAG, LangChain, vector search.

---

## AI Job Agent

**Technologies:** Python, APScheduler, SentenceTransformers, Gemini, Groq Llama, PyPDF, Pandas, Telegram Bot API

An autonomous AI agent that searches jobs, parses resumes, computes semantic similarity, verifies fresher roles with LLMs, and sends Telegram alerts.

- Architecture: Scheduler → job APIs → resume parser → embeddings → cosine similarity → Gemini/Groq evaluation → Telegram.
- Features automated job search, resume matching, semantic search, duplicate filtering and notifications.
- Skills demonstrated: embeddings, semantic search, cosine similarity, prompt engineering, resume parsing.

---

## AI First Aid Assistant

**Technologies:** Python, Flask, Google Gemini 1.5 Flash, Google Generative AI SDK, HTML, CSS, JavaScript

An AI-powered healthcare assistant providing first-aid guidance using Google's Gemini model, supporting text and image inputs for symptom analysis.

- Architecture: User → Flask → validation → text/image processing → Gemini 1.5 Flash → recommendation → web UI.
- Features text and image-based first aid, multimodal AI, secure API handling and a responsive UI.
- Skills demonstrated: Flask, prompt engineering, multimodal AI, REST APIs, image processing.

---

## Revision Bot

**Technologies:** Python, Streamlit, SQLite, SQLAlchemy, Pandas, Requests

A LeetCode revision assistant that imports solved questions, stores them in SQLite, and generates daily revision schedules through Streamlit.

- Architecture: LeetCode → importer → SQLite → difficulty analysis → revision selector → Streamlit dashboard.
- Features daily revision generation, progress tracking, question categorization and a dashboard.
- Skills demonstrated: automation, SQLAlchemy, Streamlit, data management.
