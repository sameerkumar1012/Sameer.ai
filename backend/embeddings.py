import json
import boto3


client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"   # Change if you're using another region
)


def get_embedding(text: str):

    body = {
        "inputText": text
    }

    response = client.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())

    return response_body["embedding"]


if __name__ == "__main__":

    embedding = get_embedding("Hello World")

    print(f"Embedding Length: {len(embedding)}")
    print(embedding[:10])