from nltk.stem.wordnet import WordNetLemmatizer
lem=WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stm=PorterStemmer()

word=input("Enter:")
print(lem.lemmatize(word,"v"))
print(stm.stem(word))
