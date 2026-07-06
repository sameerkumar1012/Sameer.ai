import boto3

from backend.config import AWS_REGION, LLM_MODEL

client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION
)


def generate_answer(question: str, chunks: list):

    # No relevant chunks retrieved
    if not chunks:
        return "I couldn't find that information in Sameer's portfolio."

    # Build context
    context = "\n\n".join(
        [
            f"### {chunk['title']}\n{chunk['content']}"
            for chunk in chunks
        ]
    )

    system = [
        {
            "text": """
You are PortfolioGPT, an AI assistant that answers questions about Sameer Kumar.

Rules:

1. Answer ONLY using the provided context.
2. Never use outside knowledge.
3. Never invent facts.
4. Never generate generic advice, email templates, interview processes,
   or recommendations unless they explicitly exist in the context.
5. If the context does not contain enough information, respond EXACTLY with:

I couldn't find that information in Sameer's portfolio.

6. Keep answers concise.
7. Use Markdown formatting.
8. Prefer bullet points when listing information.
"""
        }
    ]

    user_prompt = f"""
Context:

{context}

Question:

{question}
"""

    response = client.converse(
        modelId=LLM_MODEL,
        system=system,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": user_prompt
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 350,
            "temperature": 0.1,
            "topP": 0.9
        }
    )

    return response["output"]["message"]["content"][0]["text"]


if __name__ == "__main__":

    chunks = [
        {
            "source": "skills.md",
            "title": "Programming",
            "content": """
- Python
- SQL
- FastAPI
- PostgreSQL
"""
        }
    ]

    answer = generate_answer(
        "What programming languages does Sameer know?",
        chunks
    )

    print(answer)