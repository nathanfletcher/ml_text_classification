from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import urllib
import csv

# import torch
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World !"

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    # Model loaded from https://huggingface.co/cardiffnlp/twitter-roberta-base-offensive/tree/main
    # model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    if request.method == "POST":
        thejson = request.json
        thejson['result'] = process(thejson['text'])
        return thejson
    return process("Good night 😊")

    # return str(model.summary())
    # resp ={}
    # resp['prediction'] = model.predict(['We love you'])
    # print("This was supposed to print right?")
    # return resp

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def softmax(x):
    """ applies softmax to an input x"""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def process(inputText):
    # Tasks:
    # emoji, emotion, hate, irony, offensive, sentiment
    # stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary
    task='offensive'
    # MODEL = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    # tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    # download label mapping
    labels=[]
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]

    print(labels)

    # PT
    model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    # model.save_pretrained(MODEL)
    text = inputText
    text = preprocess(text)
    tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-offensive")
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Printing scores
    # return scores.tolist()

    # # TF
    # model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)
    # model.save_pretrained(MODEL)
    # text = "Good night 😊"
    # encoded_input = tokenizer(text, return_tensors='tf')
    # output = model(encoded_input)
    # scores = output[0][0].numpy()
    # scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    results = {}
    for i in range(scores.shape[0]):
        l = labels[ranking[i]]
        s = scores[ranking[i]]
        results[labels[ranking[i]]] = str(s)
        print(f"{i+1}) {l} {np.round(float(s), 4)}")
    print("These are the results")
    print(results)
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'] if os.environ['PORT'] else '8888' )