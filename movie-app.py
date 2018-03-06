from flask import Flask
from flask import request
from RequestHandler import RequestHandler

app = Flask(__name__)

rh = RequestHandler()


@app.route('/webhook', methods=['POST'])
def webhook():
    app.logger.info('Got request message = {%s}', request )
    return rh.handle_request(request.get_json()).toJSON()


if __name__ == '__main__':
    app.run()