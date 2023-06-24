import streamlit as st
from langchain.llms import OpenAI

st.title(ArushGPT ⚡)
openai_api_key = st.sidebar.text_input('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')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter OpenAI API key!', icon='🚨')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
