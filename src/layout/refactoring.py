import streamlit as st
import json
import os
import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")


def get_response(question, language):
    """
    Get the response from the Codestral API
    """
    output = {
        "prefix": "A description of the code solution",
        "programming_language": language,
        "imports": "The imports",
        "code": "The functioning code block. Write the whole code in a single line and use \t and \n for tab and new line",
        "sample_io": "Generate the sample input and output for the code generated {'input': '', 'output': ''}",
    }

    model = "codestral-latest"
    messages = [
        {
            "role": "system",
            "content": f"""You're a coding assistant. Ensure any code you provided can be executed with all required imports and variables defined. 
 Structure your answer in the JSON format: {output}

Here's the question: """,
        },
        {"role": "user", "content": question},
    ]

    headers = {"Authorization": f"Bearer {api_key}"}

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
    response = res
    response = json.loads(response)
    return response

# Custom CSS styles
st.markdown("""
<style>
/* Sidebar styles */
.sidebar .sidebar-content {
    background-image: linear-gradient(#ff66c4, #00B9E8);
    color: white;
    padding: 20px;
    border-radius: 10px;
}

header {
    background-color: #00B9E8;
    color: white;
    padding: 10px 0;
    text-align: center;
    border-radius: 10px;
    margin-bottom: 20px;
}
h1 { color: #00B9E8; }
.stButton>button {
    background-color: #C51E3A;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
}

.stButton>button:hover {
    background-color: #960018;
    color: white;
}

.stTextInput>div>div>input {
    background-color: #f0f2f6;
    color: black;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #ccc;
}

.uploaded-file {
    background-color: #fff;
    border: 1px solid #2e7bcf;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 20px;
}

code {
    background-color: #2e7bcf;
    color: #fff;
    padding: 5px;
    border-radius: 5px;
}

.footer {
    text-align: center;
    margin-top: 20px;
}

.footer a {
    color: #2e7bcf;
    text-decoration: none;
    font-weight: bold;
}

.footer a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

def code_refactoring(refactor_options: Dict) -> None:

    # Show title and description.
    st.title("RefactorGenie 💬🧞")
    st.write(
        "Refactor Coding Page"
    )
    # Conversation container
    st.markdown("Hi, this is your RefactorGenie, let's refactor your code!")

    # Upload code file
    file_types = ["py", "ts", "js"]
    uploaded_file = st.file_uploader(
        "Upload your Python, TypeScript, or JavaScript code file", type=file_types
    )

    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1]
        code = uploaded_file.read().decode("utf-8")
        st.markdown(
            f'<div class="uploaded-file"><pre><code>{code}</code></pre></div>',
            unsafe_allow_html=True,
        )

        # User input
        user_input = st.text_input("Enter additional code (optional).")

        # Button to send user input
        if st.button("REFACTOR"):
            if user_input:
                st.markdown("**Additional Code**")
                st.code(user_input, language=file_extension)
                total_code = code + "\n" + user_input
            else:
                total_code = code

            # Get response from Codestral API
            response = get_response(total_code, file_extension)

            # Process the response and provide refactored solutions
            # For demonstration purposes, we'll just display the response
            st.markdown("Here is your refactored code:")
            st.write(response)

        # Instructions for users
        st.markdown("Upload your code file or enter additional code and click REFACTOR to get refactored solutions.")

        # Instructions for users
    st.markdown("Upload your code file or enter your code in the text box and click SEND to get refactored solutions.")

    # Footer with social links
    st.markdown("""
    <div class="footer">
        <p>Follow us on:</p>
        <a href="https://www.github.com" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    return
  
if __name__ == "__main__":
    pass
