from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict,Literal,Optional
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)


json_schema={
    "title":"Student",
    "description":"Schema about students",
    "type":"object",
    "properties":{
        "name":"string",
        "age":"integer"
    },
    "required":["name"]
}

model=ChatHuggingFace(llm=llm)

structured_output=model.with_structured_output(json_schema)

result=structured_output.invoke("""The dress is good but the quality of the material is not good, there are stains present at some places as well. Disappointed in the product""")

print(result)


##DOES NOT WORK CAUSE HUGGINGFACE MODEL USED DOES NOT SUPPORT WITH_STRUCTURED_OUTPUT FUNCTION (WILL WORK WITH OPENAI)