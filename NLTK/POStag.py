from nltk import pos_tag,word_tokenize

sentence=input("Enter: ")
tokens=word_tokenize(sentence)
print( pos_tag(tokens))
