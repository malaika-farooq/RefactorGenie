import os
import requests
from dotenv import load_dotenv

def get_code_completion(prompt):
    # Load environment variables from the .env file
    load_dotenv()

    api_key = os.getenv("MISTRAL_API_KEY")

    # Check if the API key was loaded correctly
    if api_key is None:
        raise ValueError("MISTRAL_API_KEY not found in the environment variables.")

    # Define the endpoint URL
    endpoint_url = "https://codestral.mistral.ai/v1/fim/completions"

    # Extract keywords from the user's prompt (simple approach: split by spaces)
    keywords = prompt.split()

    # Create the suffix from the keywords
    suffix = " ".join(keywords)

    # Create the request payload
    payload = {
        "model": "codestral-latest",  # or the appropriate model identifier
        "prompt": prompt,
        "suffix": suffix,
    }

    # Set the headers for the request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        # Make the POST request to the specified endpoint
        response = requests.post(endpoint_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Return the response content
        return data['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"
