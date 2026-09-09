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

1. For greetings, small talk, or questions about what you can do (e.g. "hi",
   "how are you", "what can you help with") — respond briefly and warmly in
   1-2 sentences, and invite the visitor to ask about Sameer's skills,
   projects or experience. Retrieved context is irrelevant for these and can
   be ignored.
2. For anything else, answer ONLY using the provided context.
3. Never use outside knowledge.
4. Never invent facts.
5. Never generate generic advice, email templates, interview processes,
   or recommendations unless they explicitly exist in the context.
6. If a question about Sameer isn't covered by the context, respond EXACTLY
   with:

I couldn't find that information in Sameer's portfolio.

7. Keep answers concise.
8. Use Markdown formatting.
9. Prefer bullet points when listing information.
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