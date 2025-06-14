from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]
messages.append(AIMessage(content=chat_model.invoke(messages).content))
print(chat_model.invoke(messages).content )