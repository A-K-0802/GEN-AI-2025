from gensim.models import LdaModel
from gensim import corpora

str1=input("Enter sentence:")
str2=input("Enter sentence:")

doc_full=[str1,str2]
doc_split=[doc.split() for doc in doc_full]

# Creating the term dictionary of our corpus, where every unique term is assigned an index.  
dictionary=corpora.Dictionary(doc_split)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above. 
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_split]


ldamodel=LdaModel(doc_term_matrix,num_topics=3,id2word=dictionary,passes=50)

print(ldamodel.print_topics())
