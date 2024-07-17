import streamlit as st
from typing import Dict
from streamlit_ace import st_ace
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
    uploaded_file = st.file_uploader("Upload your Python code file", type="py")
    if uploaded_file:
        code = uploaded_file.read().decode("utf-8")
        st.markdown(f'<div class="uploaded-file"><pre><code>{code}</code></pre></div>', unsafe_allow_html=True)

    # User input
    user_input = ( get_user_provided_code(refactor_options["refactor_options"]["programming_language"].lower()))
    # user_input = st_ace(language='python', theme='monokai', keybinding='vscode', font_size=14, height=300)

    # Button to send user input
    if st.button("SEND"):
        if user_input:
            st.markdown("**User Input**")
            st.code(user_input, language="python")
            # Here you would typically process the code and provide refactored solutions
            # For demonstration purposes, we'll just display some example solutions
            st.markdown("Here is your refactored code:")
            st.markdown("**Solution 1**")
            st.code("def example_solution_1():\n    pass", language="python")
            st.markdown("**Solution 2**")
            st.code("def example_solution_2():\n    pass", language="python")
        else:
            st.error("Please enter your code.")

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

def get_user_provided_code(language_input: str) -> str:
    """
    Gets user-provided code using the ACE editor component.

    Args:
        language_input (str): The programming language for syntax highlighting.

    Returns:
        str: The user-provided code.
    """
    return st_ace(
        language=language_input,
        theme="monokai",
        key="ace_code_input",
        height=400,
        keybinding="vscode",
        auto_update=True,
        wrap=True,
        font_size=13,
    )
    
if __name__ == "__main__":
    pass
