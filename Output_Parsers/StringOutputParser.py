from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

template_1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)


template_2=PromptTemplate(
    template='Write a detailed summary on following text./n {text}',
    input_variables=['text']
)

prompt1=template_1.invoke({'topic':"Blackhole"})

result1=model.invoke(prompt1)

prompt2=template_2.invoke({'text':result1.content})

result_final=model.invoke(prompt2)

print(result_final.content)
