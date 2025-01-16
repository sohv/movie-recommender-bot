import streamlit as st
from langchain_openai import ChatOpenAI

# create llm instance
llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)

# create the Embedding model
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
'''
import cohere
from langchain.chat_models import ChatCohere
from langchain.embeddings import CohereEmbeddings

cohere_api_key = st.secrets["COHERE_API_KEY"]

llm = ChatCohere(
    cohere_api_key=cohere_api_key,
    model="command-xlarge-20221108", 
)

embeddings = CohereEmbeddings(
    cohere_api_key=cohere_api_key
)
'''