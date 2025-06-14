from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage,SystemMessage


#chat template
chat_temp=ChatPromptTemplate([
    ('system','You are a helful customer suppport agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','Where is my refund?')
])

chat_history=[]
#load chat history
with open('Prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())


#create prompt

prompt=chat_temp.invoke({'chat_history':chat_history})

print(prompt)