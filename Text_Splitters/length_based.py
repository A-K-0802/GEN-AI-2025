from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader('poem.txt')
doc=loader.load()

splitter= CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result=splitter.split_documents(doc)
print(result)