from flask import Flask
from flask import request
from flask import json
from FilmwebManager import FilmwebManager

app = Flask(__name__)

filmweb = FilmwebManager()


@app.route('/', methods=['POST'])
def hello_world():

    data = request.get_json()
    return data['name']


@app.route('/movie/best', methods=['GET'])
def get_best_movie():
    return filmweb.get_best_movie()


if __name__ == '__main__':
    app.run()
