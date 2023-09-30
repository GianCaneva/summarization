from transformers import pipeline
from bias_remover import remove_bias
summarizer = pipeline("summarization", model="LeoCordoba/mt5-small-mlsum")

def summarize_text(request):

    received_text = request.data.decode('utf-8')
    textExtension = request.args.get('textExtension')
    
    #print("Received Text:", received_text)
    #print("Max extension value:", max_text_extension)
    #print("Min extension value:", min_text_extension)

    #print(summarizer(article, max_length=20, min_length=5))
    ##for titles: 20/5
    response = summarizer(remove_bias(received_text), max_length=int(textExtension)+100, min_length=int(textExtension))[0]['summary_text']
    print ("Model 2:" + response)
    return response



