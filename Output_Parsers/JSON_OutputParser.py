from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template_1=PromptTemplate(
    template='Give me name, age and city of a fictional person.\n{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=  template_1 | model | parser
result=chain.invoke({})
print(result)