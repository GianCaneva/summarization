import spacy
from spacy.lang.es.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

## Process responsible for getting keywords of a text using NLP
def getKeywords(request):

    nlp = spacy.load(name="es_dep_news_trf")
    text = request.data.decode('utf-8')
    doc=nlp(text.lower())

    len(list(doc.sents))

    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)

    freq_word = Counter(keyword).most_common(5)
    palabras = [palabra for palabra, _ in freq_word]
    cadena_palabras = ', '.join(palabras)

    #print("palabras"+palabras)
    print("cadena"+cadena_palabras)

    return palabras

text0 = '''La oposición salió a cuestionar el fallo judicial que ordenó la liberación de "Chocolate" Rigau, al asegurar que tendría el objetivo de garantizar el silencio del acusado y, de esa forma, evitar un pronto esclarecimiento del supuesto entramado de corrupción que ventilaron las maniobras perpetradas en los cajeros automáticos de un banco de La Plata. Entre los referentes opositores también crece el temor de que el hecho provoque un crecimiento del discurso antipolítica.

Para la diputada nacional Margarita Stolbizer, la resolución de la Cámara de Apelaciones platense basa "en una detención mal hecha, pero la causa no desaparece", por lo que se mostró confiada en una pronta apelación del fiscal de cámara.

Para la líder del GEN, detrás de la rápida liberación de Rigau habría "un encubrimiento de la política. Vemos cómo la justicia termina siendo cómplice para que no sepa la cuestión de fondo, qué hay detrás de ese accionar. Nadie puede pensar que esta persona se quedaba con todos esos millones de pesos", en clara alusión a que habría una estructura política detrás del implicado.

En este sentido, Stolbizer planteó a sus legisladores provinciales la necesidad de "apurar" una ley de financiamiento político en la Provincia. "De lo contrario, nos 'enchastran' a todos y después nos sorprendemos porque la gente vota a Milei", analizó en diálogo con este diario.

Si bien reconoció que no es delito encontrar a una persona sacando plata de un cajero, observó que "hay que insistir en el fondo de la cuestión, para quién operaba" el acusado. "Lo van a tener que custodiar porque hay mucho interés en que no hable. Su liberación es para que no se investigue a fondo" el caso, conjeturó.'''