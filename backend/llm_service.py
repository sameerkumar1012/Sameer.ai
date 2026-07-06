import boto3
from backend.config import AWS_REGION, LLM_MODEL

client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION
)


def generate_answer(question: str, chunks: list):

    context = "\n\n".join(
        [
            f"## {chunk['title']}\n{chunk['content']}"
            for chunk in chunks
        ]
    )

    system = [
        {
            "text": (
                "You are PortfolioGPT.\n"
                "Answer ONLY using the provided context.\n"
                "Do not make up information.\n"
                "Respond in beautiful Markdown.\n"
                "Be concise and professional."
            )
        }
    ]

    response = client.converse(
        modelId=LLM_MODEL,
        system=system,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": f"""
Context:

{context}

Question:

{question}
"""
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 400,
            "temperature": 0.2,
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