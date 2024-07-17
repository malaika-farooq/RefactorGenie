import json
import os

import cohere
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key=cohere_api_key)

response = co.chat(
    model="command-r-plus",
    message="What is the chemical formula for glucose?",
    connectors=[{"id": "web-search"}],
)

print(response)
