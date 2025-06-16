from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['HUGGINGFACEHUB_API_TOKEN']="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"
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

temp=PromptTemplate(
    template='Give a summary of the {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader=TextLoader('Doc_loader/poem.txt')

docs=loader.load()

chain= temp | model | parser

print(chain.invoke({'poem': docs[0].page_content}))