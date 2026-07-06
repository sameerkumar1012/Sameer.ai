import json
import boto3
from backend.config import AWS_REGION, EMBEDDING_MODEL

client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)


def get_embedding(text: str):

    body = {
        "inputText": text
    }

    response = client.invoke_model(
        modelId=EMBEDDING_MODEL,
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())

    return response_body["embedding"]


if __name__ == "__main__":

    embedding = get_embedding("Hello World")

    print(f"Embedding Length: {len(embedding)}")
    print(embedding[:10])