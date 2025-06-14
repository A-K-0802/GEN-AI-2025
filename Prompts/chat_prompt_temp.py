from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

chat_temp=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in breif about {topic}')
])

prompt=chat_temp.invoke({'domain':"Cricket expert",'topic':'White season ball'})

print(prompt)