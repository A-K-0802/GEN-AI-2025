from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

st.header("Chat BOT")
user_input=st.text_input("Input here")

if st.button("Send input"):
    response=chat_model.invoke(user_input)
    st.write(response.content)