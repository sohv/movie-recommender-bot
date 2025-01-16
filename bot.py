import streamlit as st
from utils import write_message
from agent import generate_response

st.set_page_config("Ebert", page_icon=":movie_camera:")

# set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the GraphAcademy Chatbot!  How can I help you?"},
    ]

# submit message
def handle_submit(message):
    """
    Submit handler:

    You have to modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # handling the response
    with st.spinner('Thinking...'):
        response = generate_response(message)
        write_message('assistant', response)


# display messages in session state
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# handle any user input
if question := st.chat_input("What is up?"):
    write_message('user', question)
    handle_submit(question)
