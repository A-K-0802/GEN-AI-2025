lookup_words={"rt":"ReTweet","dm":"Direct Message"}

def standardize(inputstr):
    words=inputstr.split()
    new_words=[]
    for wrd in words:
        if wrd.lower() in lookup_words:
            wrd=lookup_words[wrd.lower()]
        new_words.append(wrd)
    new_str=" ".join(new_words)
    return new_str

print(standardize("DM me"))
    

    