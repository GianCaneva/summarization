from transformers import pipeline
from bias_remover import remove_bias
summarizer = pipeline("summarization", model="LeoCordoba/mt5-small-mlsum")

def summarize_text(request):

    received_text = request.data.decode('utf-8')
    max_text_extension = request.args.get('maxTextExtension')
    min_text_extension = request.args.get('minTextExtension')
    
    print("Received Text:", received_text)
    print("Max extension value:", max_text_extension)
    print("Min extension value:", min_text_extension)

    #print(summarizer(article, min_length=5, max_length=20))
    ##for titles: 5/20
    return summarizer(remove_bias(received_text), max_length=int(max_text_extension), min_length=int(min_text_extension))



