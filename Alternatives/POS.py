
import urllib3
import warnings

# Desactiva las advertencias específicas de urllib3
urllib3.disable_warnings()
# Configura el filtro de advertencias para ignorar todas las advertencias
warnings.filterwarnings("ignore")
import spacy
# Sample
texto_ejemplo = "Soy Gianfranco y estoy probando un corto mensaje sobre el uso de ésta funcionalidad."
nlp = spacy.load("es_core_news_lg")
doc = nlp(texto_ejemplo)
print(doc.text)
for token in doc:
    print(f"{token.text:20} {token.pos_:20} {token.dep_:20} {spacy.explain(token.pos_)}")