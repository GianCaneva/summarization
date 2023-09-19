import json
from flask import Flask, request, jsonify
from bias_remover import remove_bias
from summarization_mt5_small_mlsum import summarize_text
#To run: python3 flask_server.py

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def receive_text():

    try:
        # Pre-trained model responsible for summmarizing text
        response = remove_bias(summarize_text(request))
        return json.dumps(response, ensure_ascii=False), 200
       
    except Exception as e:
        print("Error:", str(e))
        response = {'error': 'There was an error processing the request.'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
