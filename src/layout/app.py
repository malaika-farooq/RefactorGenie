import streamlit as st
from layout import page_config, code_refactoring, homepage, navbar
from layout.sidebar import sidebar
#from utils.arctic_operations import ArcticOps


def init_session_state():
    if "selected_functionality" not in st.session_state:
        st.session_state["selected_functionality"] = None


def run_app():
    # st.set_page_config(page_title="RefactorGenie", page_icon="🧞", layout="wide")
    page_config()
    page = navbar()
    init_session_state()

    options = sidebar(page)
    
    # if page != "Home":
    #     options = sidebar(page)
    # else:
    #     options = None
    get_page_contents(page, options)

def get_page_contents(page, options):
    if page == "Home":
        homepage()
    elif page == "RefactorLab":
        code_refactoring(options)
    # elif page == "UploadFile":
    #     data_analysis(options)