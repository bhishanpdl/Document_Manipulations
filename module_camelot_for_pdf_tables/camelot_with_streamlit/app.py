# imports
import streamlit as st
import os
import sys
import glob

import openai
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain.llms import AzureOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# local imports
from src.html_templates import css, bot_template, user_template
from src.util_text import get_lst_text_from_uploaded_file
from src.util_doc import get_doc_chunks_from_lst_text
from src.util_prompts import gen_prompt
from src.util_llm import get_vectorstore_from_doc_chunks, get_conversation_chain
from src.util_streamlit import display_conversation
from src.util_streamlit import handle_userinput
from src.config import config

MODEL = 'gpt-35-turbo-16k'
TEMP = 0.0
prompt = gen_prompt

def init_ses_states():
    session_states = {
        "conversation": None,
        "chat_history": None,
        "questions": None,
        "prompt_and_question": "",
    }
    for state, default_value in session_states.items():
        if state not in st.session_state:
            st.session_state[state] = default_value

def process_docs_st(uploaded_files, TEMP, config):
    # document is processed only once and a conversation chain is created.
    # then, we qa the chain multiple time (we do not process same document multiple times)
    st.session_state["conversation"] = None
    st.session_state["chat_history"] = None
    st.session_state["questions"] = []
    st.session_state["prompt_and_question"] = ""
    st.session_state["response"] = None

    all_doc_chunks = []
    for i, uploaded_file in enumerate(uploaded_files):
        file_name = uploaded_file.name
        lst_text = get_lst_text_from_uploaded_file(uploaded_file,ocr=True,pytesseract_path=None)
        doc_chunks = get_doc_chunks_from_lst_text(lst_text,file_name)

        for doc in doc_chunks:
            doc.metadata["pdf_number"] = str(i+1)
            all_doc_chunks.append(doc)

    vectorstore = get_vectorstore_from_doc_chunks(all_doc_chunks)
    conv_chain = get_conversation_chain(vectorstore, temp=TEMP, config=config)

    st.session_state.conversation = conv_chain
    st.session_state.prompt_and_question = ""
    st.session_state.pdf_processed = True

def sidebar():
    global uploaded_files
    global config

    with st.sidebar:
        st.header('Instructions:')
        st.write('1. Upload the pdf (scanned or regular)')
        st.write('2. Click: Process Files + New Chat')
        st.write('3. Start chatting with the chatbot')

        # processing
        with st.expander("Your Documents", expanded=True):
            uploaded_files = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
            if st.button("Process Files + New Chat"):
                if uploaded_files:
                    # process uploaded files
                    with st.spinner("Processing"):
                        process_docs_st(uploaded_files, TEMP, config)
                else:
                    st.caption("Please Upload At Least 1 PDF")
                    st.session_state.pdf_processed = False

def main():
    st.set_page_config(page_title="Multi-Document Chat Bot", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    global uploaded_files, config

    prompt = gen_prompt

    init_ses_states()
    tabs = st.tabs(["Chatbot"] )

    # tab: deploy
    with tabs[0]:
        st.title(":books: PDF Chatbot")
        st.subheader("Created by: Bhishan Poudel")
        sidebar()

        # pdf is processed
        if st.session_state.get("pdf_processed"):
            with st.form("user_input_form"):
                user_question = st.text_input("Ask a question about your documents:")
                send_button = st.form_submit_button("Send")
            if send_button and user_question:
                handle_userinput(user_question, prompt)

        # pdf is not processed
        if not st.session_state.get("pdf_processed"):
            st.caption("Please Upload Atleast 1 PDF Before Proceeding")

if __name__ == '__main__':
    main()
