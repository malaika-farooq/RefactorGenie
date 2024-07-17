import json
import os
import requests
import cohere
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
mistral_api_key = os.getenv("MISTRAL_API_KEY")
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize the Cohere client
co = cohere.Client(api_key=cohere_api_key)

def get_codestral_response(question):
    """
    Get the response from the Codestral API
    """
    output = {
        "prefix": "A description of the code solution",
        "programming_language": "The programming language",
        "imports": "The imports",
        "code": "The functioning code block. Write the whole code in single line and use \t and \n for tab and new line",
        "sample_io": "Generate the sample input and output for the code generated {'input': '', 'output': ''}",
    }

    model = "codestral-latest"
    messages = [
        {
            "role": "system",
            "content": f"""You're a coding assistant. Ensure any code you provided can be executed with all required imports and variables defined. \n
                Structure your answer in the JSON format: {output}

                Here's the question: """,
        },
        {"role": "user", "content": question},
    ]

    headers = {"Authorization": f"Bearer {mistral_api_key}"}

    res = requests.post(
        "https://codestral.mistral.ai/v1/chat/completions",
        headers=headers,
        json={
            "model": model,
            "messages": messages,
            "response_format": {"type": "json_object"},
        },
    )
    res = res.json()
    response = res["choices"][0]["message"]["content"]
    response = response.replace("```python", "")
    response = response.replace("```", "")
    response = json.loads(response)
    return response

def get_cohere_response(question):
    """
    Get the response from the Cohere API
    """
    response = co.chat(
        model="command-r-plus",
        message=question,
        connectors=[{"id": "web-search"}],
    )
    return response

def main(question):
    codestral_response = get_codestral_response(question)
    cohere_response = get_cohere_response(question)
    
    combined_response = {
        "codestral": codestral_response,
        "cohere": cohere_response
    }
    
    return combined_response

if __name__ == "__main__":
    question = input("Please enter your question: ")
    response = main(question)
    print(response)
