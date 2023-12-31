import os
os.system("python3 -m ensurepip --upgrade")
os.system("pip3 install es_dep_news_trf")

import json
from flask import Flask, request, jsonify
from bias_remover import remove_bias
#Model 1
#from summarization_mt5_base_dacsa_es import summarize_text
#Model 2
#from summarization_mt5_small_mlsum import summarize_text as summarize_text_2
#Model 3
from summarization_spacy import summarize_text
from keywords_spacy import getKeywords

from title_generator import generate_summary
#To run: python3 main.py

app = Flask(__name__)

@app.route('/api/summarize/article', methods=['POST'])
def receive_text():

    try:
        # Pre-trained model responsible for summmarizing text
        response = remove_bias(summarize_text(request))
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500
    

@app.route('/api/summarize/title', methods=['POST'])
def receive_title():
    try:
        # Pre-trained model responsible for summmarizing text
        response = remove_bias(generate_summary(request))
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500


@app.route('/api/keywords', methods=['POST'])
def receive_keywords():
    try:
        # Pre-trained model responsible for summmarizing text
        response = getKeywords(request)
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500
    
@app.route('/api/bias', methods=['POST'])
def receive_unbiased():
    try:
        # Pre-trained model responsible for summmarizing text
        response = remove_bias(request)
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500
    
@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    try:
        # Pre-trained model responsible for summmarizing text
        return json.dumps("Application UP", ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
