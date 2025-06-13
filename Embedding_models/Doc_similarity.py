from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document=["Dreams begin where fear ends.","Rain kissed the quiet earth.","Stars whispered secrets to night.","Hope blooms even in darkness.","The cat danced under moonlight."]

query="Tell me about cat who danced"

doc_emb=embedding.embed_documents(document)
que_emb=embedding.embed_query(query)

scores=cosine_similarity([que_emb],doc_emb)
print(sorted(list(enumerate(scores)),key=lambda x:x[1]))

scorelist=sorted(list(enumerate(scores)),key=lambda x:x[1])
print(scorelist)
