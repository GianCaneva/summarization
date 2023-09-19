import spacy
#Requisitos
#pip3 install spacy
#python3 -m spacy download es_core_news_lg


def remove(texto):
    # Loads spacy module
    nlp = spacy.load("es_core_news_lg")
    
    # Text process
    doc = nlp(texto)
    
    # Non-adjetive list
    non_adj_words = []
    
    # Check if the previous token was an adjetive
    previous_adj = False
    previous_token = ""

    # Iterate through the tokens in the text
    for token in doc:
        if token.pos_ == "ADJ":
            # If the current token is an adjective and the previous one was also an adjective, skip the current token
            if previous_adj:
                continue
            # If the previous token was an adjective, check to see if there is a comma or connector before it
            if previous_adj and (token.text == "," or token.text.lower() in ["y", "u"]):
                continue
            # If the previous token was an adjective, check to see if there is a comma or connector before it. If it is, remove the last element in the Non-Adjetive list
            if previous_adj and (previous_token == "," or previous_token.lower() in ["y", "u"]):
                non_adj_words.pop()
            previous_adj = True
        elif (token.text == "," or token.text.lower() in ["y", "u"]):
            continue
        else:
            previous_adj = False
            non_adj_words.append(token.text)

        previous_token = token.text
        
 
    # Join the words in a text string
    text_without_adjetives = " ".join(non_adj_words)
    
    # return text without adjetives and extra spaces in the text
    return text_without_adjetives.strip()

# Sample
texto_ejemplo = "Este es un hermoso, cálido y soleado día de verano."
texto_sin_adjetivos = remove(texto_ejemplo)
