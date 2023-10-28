import spacy
#from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.es.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
nlp = spacy.load("es_dep_news_trf")

## Process responsible for summarizing articles and create a new one that includes all of them but shorter
def summarize_text(request):

    text = request.data.decode('utf-8')
    textExtension = request.args.get('textExtension')
    print("////////////0/////")
    print(textExtension)
    #required mapping to adapt previous model
    extension_mapping = {
        '100': 3,
        '200': 6,
        '300': 9,
        '400': 11,
        '500': 12,
        '600': 13,
        '700': 14,
    }

    article_Extension = extension_mapping.get(textExtension, "Valor de textExtension no válido.")
    print("////////////1/////")
    print(article_Extension)

    doc=nlp(text)

    len(list(doc.sents))

    keyword = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    for token in doc:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keyword.append(token.text)

    freq_word = Counter(keyword)
    print(freq_word.most_common(5))
    type(freq_word)
    max_freq = Counter(keyword).most_common(1)[0][1]
    for word in freq_word.keys():  
            freq_word[word] = (freq_word[word]/max_freq)
    freq_word.most_common(5)
    sent_strength={}
    for sent in doc.sents:
        for word in sent:
            if word.text in freq_word.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
                else:
                    sent_strength[sent]=freq_word[word.text]
    #print(sent_strength)
    #print("")
    summarized_sentences = nlargest(article_Extension, sent_strength, key=sent_strength.get) 

   

    print("////////////1/////")
    print(summarized_sentences)
    print("////////////2/////")
    print(summarized_sentences[0])
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    print("////////////3/////")

    print(summary)
    return summary


    #[('liberación', 3), ('fondo', 3), ('Rigau', 2), ('acusado', 2), ('Stolbizer', 2)]