import os
import streamlit as st

from openai import OpenAI

client = OpenAI(api_key=st.secrets("OPENAI_API_KEY"))

def call_llm(messages, temperature=0.7):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content