from flask import Flask
from flask import request
from RequestHandler import RequestHandler
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

rh = RequestHandler()


@app.route('/webhook', methods=['POST'])
def webhook():
    json = request.get_json()
    app.logger.info("Got request message = {%s}", json)
    response = rh.handle_request(json)
    app.logger.info("sending response = {%s}", response)
    return response


if __name__ == '__main__':
    app.run()