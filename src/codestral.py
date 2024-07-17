import json
import os

import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

def get_response(question):
    """
    Get the response from the Codestral API
    """
    output = {
        "prefix": "A description of the code solution",
        "programming_language": "The programming language",
        "imports": "The imports",
        "code": "The functioning code block. Write the whole code in single line and use \t and \n for tab and new line",
        "sample_io": "Generate the sample input and output for the code generated {'input': '', 'output': ''}"
    }

    model = "codestral-latest"
    messages = [{
                "role": "system",
                "content": f"""You're a coding assistant. Ensure any code you provided can be executed with all required imports and variables defined. \n
                Structure your answer in the JSON format: {output}

                Here's the question: """
            }, {"role": "user", "content": question}]


    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    res = requests.post(
        "https://codestral.mistral.ai/v1/chat/completions",
        headers=headers,
        json ={
            "model": model,
            "messages": messages,
            "response_format": {"type": "json_object"}
        }
    )
    res = res.json()
    response = res["choices"][0]["message"]["content"]
    response = response.replace("```python", "")
    response = response.replace("```", "")
    print(response)
    response = json.loads(response)
    return response