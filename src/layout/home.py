import streamlit as st


def homepage():
    # set_page_width(900)
    st.markdown(
        """
    # 🧞💬 RefactorGenie: Your AI Code Refactor Assistant!"""
    )
    st.markdown("Hi, let's refactor your code!")
    # Show title and description.
    st.markdown(
        "This is a simple chatbot that uses Mistral AI and Cohere model to generate responses."
    )

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
    st.markdown("""
    Welcome to RefactorGenie, your AI-powered assistant for effortless code refactoring and optimization. Here's how to get started:
    
    ### Refactor Your Code:
    1. **Navigate to the "Refactor Code" Tab**: Begin by selecting the "Refactor Code" tab on the homepage.
    2. **Input Your Code**: Enter your code in the provided code section.
    3. **Get Your Output**: Click the submit button to receive refactored, optimized code solutions.
    
    ### Upload a File:
    1. **Go to the "Upload File" Section**: Select the "Upload File" tab on the homepage.
    2. **Upload Your File**: Choose and upload your Python code file.
    3. **Get Your Desired Output**: The tool will process the file and provide you with the refactored output.
    
    Our goal is to make code refactoring seamless, efficient, and accessible, helping you achieve cleaner, more optimized code with ease.
    """, unsafe_allow_html=True)
    return