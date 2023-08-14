import nltk
from nltk.corpus import stopwords
from tqdm import tqdm
import time as ti

def normalize(s):
    replacements =  (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s= s.replace(a, b).replace(a.upper(), b.upper())
    return s


def token():
    content = "hola como andas todo bien"
    tokenize = nltk.word_tokenize(content)
    print (tokenize)
    '''
    token_limpio = []
    guardar = True
    for i in tqdm(tokenize):
        for word in stopword.words('spanish'):
            if(word.lower() = i.lower()):
                guardar = False
        if ( guardar): 
            if ( len(i) > 2): 
                token_limpio.append(normalize(i))
        guardar = True

    print(token_limpio)
    '''