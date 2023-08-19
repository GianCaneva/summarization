from flask import Flask, request, jsonify
import json
from transformers import pipeline
summarizer = pipeline("summarization", model="ELiRF/mt5-base-dacsa-es")
#This is the one what works
#To run: python3 flask_server.py


app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def receive_text():
    try:
        received_text = request.data.decode('utf-8')
        print("Texto recibido:", received_text)
        response = summarizer(received_text, max_length=400, min_length=300, do_sample=False)
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'Hubo un error al procesar la solicitud.'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
