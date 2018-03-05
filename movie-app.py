from flask import Flask
from flask import request
from flask import json
from flask import jsonify

from RequestHandler import RequestHandler

app = Flask(__name__)

rh = RequestHandler()


@app.route('/webhook', methods=['POST'])
def webhook():
    return rh.handle_request(request.get_json())


# @app.route('/movie/best', methods=['POST'])
# def get_best_movie():
#     return filmweb.get_best_movie().url


if __name__ == '__main__':
    app.run()
