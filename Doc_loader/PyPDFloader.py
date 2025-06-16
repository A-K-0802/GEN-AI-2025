from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Doc_loader/Langchain_pdf.pdf')

docs=loader.load()

print(docs[0].page_content)
print(docs[0].metadata)

