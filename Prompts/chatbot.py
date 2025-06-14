from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)
chat_history=[
    SystemMessage(content='You are helpful AI assistant')]
while True:
    user_input=input("YOU: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)