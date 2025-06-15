from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

class review(TypedDict):
    Summary:str
    sentiment: str

model=ChatHuggingFace(llm=llm)

structured_output=model.with_structured_output(review)

result=structured_output.invoke("""The dress is good but the quality of the material is not good, there are stains present at some places as well. Disappointed in the product""")

print(result)


