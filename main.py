## Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain_community.llms import OpenAI 
from langchain.llms import OpenAI 

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text=st.text_input("Search the topic you want")

#OPEN AI LLMs
#llm=OpenAI(openai_api_key = openai_key,model_name = 'gpt-3.5-turbo-1106',temperature=0.8)
llm=OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))

