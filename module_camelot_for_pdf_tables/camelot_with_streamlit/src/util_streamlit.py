import streamlit as st
import base64
import os
import glob

# local imports
from src.html_templates import css, bot_template, user_template

def display_conversation(prompt):
    r"""Display Conversation

    Depends:
    ========
    - bot_template
    - user_template

    """
    with st.container():
        for i, this_chat_hist in enumerate(reversed(st.session_state.chat_history)):

            question = this_chat_hist.content[len(prompt):]
            answer = this_chat_hist.content

            if i % 2 == 0: # 0,2,4 etc are Bot answer
                st.markdown(bot_template.replace("{{MSG}}", answer), unsafe_allow_html=True)
            else: # 1,3,5 etc are User questions
                st.markdown(user_template.replace("{{MSG}}", question), unsafe_allow_html=True)

def handle_userinput(user_question, prompt):
    response = st.session_state.conversation({'question': (prompt+user_question)})
    st.session_state.response = response
    st.session_state.chat_history = response['chat_history']
    st.session_state.prompt_and_question = response['question']
    st.session_state.questions.append(st.session_state.prompt_and_question)

    # display the conversation
    with st.spinner('Generating response...'):
        display_conversation(prompt)
