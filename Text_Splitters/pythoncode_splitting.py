from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


code="""
class review(BaseModel):
    
    key_themes:list[str]=Field(description="Write all themes discussed in the review")
    summary:str=Field(description="Write the summary of the review")
    sentiment:Literal['pos','neg']=Field(description="Write the sentiment of the review")
    pros:Optional[list[str]]=Field(default=None,description="Write pros of product")
    cons:Optional[list[str]]=Field(default=None,description="Write cons of product")
    name:Optional[str]=Field(default=None,description="Write the name of reviewer")

model=ChatHuggingFace(llm=llm)

structured_output=model.with_structured_output(review)

print(result)
"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)

result=splitter.split_text(code)
print(result)