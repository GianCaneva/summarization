import spacy
#Requisitos
#pip3 install spacy
#python3 -m spacy download es_core_news_lg


def remove(texto):
    # Carga el modelo spacy
    nlp = spacy.load("es_core_news_lg")
    
    # Procesa el texto
    doc = nlp(texto)
    
    # Inicializa una lista para almacenar las palabras que no son adjetivos
    palabras_no_adj = []
    
    # Variable para rastrear si el token anterior fue un adjetivo
    adj_anterior = False
    token_ant = ""

    # Recorre los tokens del texto
    for token in doc:
        if token.pos_ == "ADJ":
            # Si el token actual es un adjetivo y el anterior también lo fue, omite el token actual
            if adj_anterior:
                continue
            # Si el token anterior fue un adjetivo, verifica si hay una coma o un conector antes
            if adj_anterior and (token.text == "," or token.text.lower() in ["y", "u"]):
                continue
            if adj_anterior and (token_ant == "," or token_ant.lower() in ["y", "u"]):
                palabras_no_adj.pop()
            adj_anterior = True
        elif (token.text == "," or token.text.lower() in ["y", "u"]):
            continue
        else:
            adj_anterior = False
            palabras_no_adj.append(token.text)

        token_ant = token.text
        
 
    # Une las palabras en una cadena de texto
    texto_sin_adjetivos = " ".join(palabras_no_adj)
    
    return texto_sin_adjetivos.strip()

# Ejemplo de uso
texto_ejemplo = "Este es un hermoso, cálido y soleado día de verano."
texto_sin_adjetivos = remove(texto_ejemplo)
