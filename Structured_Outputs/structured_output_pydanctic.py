from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict,Literal,Optional
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation'
)

class review(BaseModel):
    
    key_themes:list[str]=Field(description="Write all themes discussed in the review")
    summary:str=Field(description="Write the summary of the review")
    sentiment:Literal['pos','neg']=Field(description="Write the sentiment of the review")
    pros:Optional[list[str]]=Field(default=None,description="Write pros of product")
    cons:Optional[list[str]]=Field(default=None,description="Write cons of product")
    name:Optional[str]=Field(default=None,description="Write the name of reviewer")

model=ChatHuggingFace(llm=llm)

structured_output=model.with_structured_output(review)

result=structured_output.invoke("""The dress is good but the quality of the material is not good, there are stains present at some places as well. Disappointed in the product""")

print(result)


##DOES NOT WORK CAUSE HUGGINGFACE MODEL USED DOES NOT SUPPORT WITH_STRUCTURED_OUTPUT FUNCTION (WILL WORK WITH OPENAI)