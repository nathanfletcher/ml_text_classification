from flask import Flask
from flask import jsonify
from flask import request
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World !"

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    return "Hello World !"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'] if os.environ['PORT'] else '8888' )