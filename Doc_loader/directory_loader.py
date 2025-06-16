from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader= DirectoryLoader(
    path="Doc_loader/DOCS",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()

print(len(docs))
print(docs[4].page_content)
print(docs[4].metadata)


##Lazy Load for many docs