from flask import Flask
from flask import jsonify
from flask import request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'] if os.environ['PORT'] else '8888' )