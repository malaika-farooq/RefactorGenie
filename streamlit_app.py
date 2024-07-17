import streamlit as st
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

    try:
        res = requests.post(
            "https://codestral.mistral.ai/v1/chat/completions",
            headers=headers,
            json={
                "model": model,
                "messages": messages,
                "response_format": {"type": "json_object"},
            },
        )
        res.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")
        return None

    try:
        res_json = res.json()
        response = res_json["choices"][0]["message"]["content"]
        response = response.replace("```python", "```")
        response = response.replace("```", "")
        response = json.loads(response)
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        st.error(f"Failed to parse API response: {e}")
        st.error(f"API response content: {res.content}")
        return None

    return response


st.set_page_config(page_title="RefactorGenie", page_icon="🧞", layout="wide")

# Show title and description.
st.title("RefactorGenie 💬🧞")
st.write(
    "This is a simple chatbot that uses Mistral AI and Cohere model to generate responses."
)

# Custom CSS styles
st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("💬🧞")
st.sidebar.markdown("### About:")
st.sidebar.markdown(
    """
**RefactorGenie** is your AI-powered assistant designed to make code refactoring easier, faster, and more efficient. 
Whether you're a developer looking to clean up your codebase, enhance code readability, or optimize performance, RefactorGenie is here to help. 
Leveraging advanced AI models, RefactorGenie analyzes your code and provides multiple refactored solutions tailored to your needs. 
Say goodbye to manual code reviews and hello to intelligent, automated refactoring.
"""
)
st.sidebar.markdown("### Steps to Use RefactorGenie:")
st.sidebar.markdown(
    """
1. **Access the Application**:
   - Open the RefactorGenie application on your web browser.

2. **Upload Your Code**:
   - Click the "Upload" button to upload your Python, TypeScript, or JavaScript code file.
   - Select the `.py`, `.ts`, or `.js` file from your device and click "Open".

3. **View Uploaded Code**:
   - Once uploaded, your code will be displayed on the screen for you to review.

4. **Submit for Refactoring**:
   - Click the "SEND" button to submit your code for refactoring.
   - The AI will process your code and generate optimized solutions.

5. **Receive Refactored Solutions**:
   - View the refactored solutions provided by RefactorGenie.
   - The solutions will be displayed on the screen, allowing you to compare and choose the best one for your needs.

6. **Implement and Enjoy**:
   - Implement the refactored code into your project.
   - Enjoy cleaner, more efficient, and optimized code!
"""
)
st.sidebar.markdown("### Social Links:")
st.sidebar.write("🔗 [GitHub](https://www.github.com)")

# Main page
# st.markdown('<header><h1>Welcome to RefactorGenie</h1></header>', unsafe_allow_html=True)

# Conversation container
st.markdown("Hi, this is your RefactorGenie, let's refactor your code!")

# Upload code file
file_types = ["py", "ts", "js"]
uploaded_file = st.file_uploader(
    "Upload your Python, TypeScript, or JavaScript code file", type=file_types
)

if uploaded_file:
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
            st.code(user_input)
            total_code = code + "\n" + user_input
        else:
            total_code = code

        # Get response from Codestral API
        response = get_response(total_code)

        if response:
            # Process the response and provide refactored solutions
            st.markdown("Here is your refactored code:")
            st.write(response)
        else:
            st.error("Failed to get a valid response from the API.")

# Instructions for users
st.markdown(
    "Upload your code file or enter additional code and click REFACTOR to get refactored solutions."
)

# Footer with social links
st.markdown(
    """
<div class="footer">
<p>Follow us on:</p>
<a href="https://www.github.com" target="_blank">GitHub</a>
</div>
""",
    unsafe_allow_html=True,
)
