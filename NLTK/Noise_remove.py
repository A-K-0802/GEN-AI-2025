noise_dictionary=['is','a','this','the']

def noise_rem(input_str):
    words=input_str.split()
    noiseless_words=[word for word in words if word not in noise_dictionary]
    new_str=" ".join(noiseless_words)
    return new_str

print(noise_rem("this is a picture"))