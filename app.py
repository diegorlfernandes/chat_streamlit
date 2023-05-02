import streamlit as st
from streamlit_chat import message
import requests
from ChatGPT import ChatGPT

st.set_page_config(
    page_title="Pizzaria",
    page_icon=":robot:"
)

st.header("Pizzaria")
    
container = st.container()

user_input = st.text_input("You: ", key="input")

if 'user' not in st.session_state:
    st.session_state['user'] = []

if 'bot' not in st.session_state:
    st.session_state['bot'] = []

 
if user_input:
    GPT = ChatGPT(st.secrets['api_key'])

    response = GPT.collect_messages(user_input)
    
    st.session_state['user'].append("Usuário: "+user_input) 
    st.session_state['bot'].append("Bot: "+response)

    if st.session_state['user']:
        with container:
            for i in range(len(st.session_state['user'])):
                message(st.session_state["user"][i], is_user=True, key=str(i) + '_user')
                message(st.session_state["bot"][i], key=str(i)+'_bot')
