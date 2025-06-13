from langchain_huggingface import HuggingFaceEmbeddings

embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs=["Delhi is capital of India","Paris is capital of France"]
vector=embedding.embed_documents(docs)

print(str(vector))