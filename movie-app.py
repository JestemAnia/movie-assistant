from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():

    data = request.get_json()
    return data['name']

@app.route('/hello/<username>')
def my_method(username):
    return 'czesc '+ username

@app.route('/dialogflow')
def dialogflow():
    return 'dialogflow'

if __name__ == '__main__':
    app.run()
