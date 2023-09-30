from transformers import pipeline
from bias_remover import remove_bias
summarizer = pipeline("summarization", model="ELiRF/mt5-base-dacsa-es")

def summarize_text(request):

    received_text = request.data.decode('utf-8')
    textExtension = request.args.get('textExtension')

    response = summarizer(remove_bias(received_text), max_length=int(textExtension)+100, min_length=int(textExtension), do_sample=False)[0]['summary_text']
    print ("Model 1:" + response)
    return response
