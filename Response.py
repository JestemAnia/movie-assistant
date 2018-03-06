import json

class Response:
    def __init__(self, message, req):
        self.speech = message
        self.displayText = message
        self.contextOut = req['result']['contexts']


    # res = {'speech': output,
    #        'displayText': output,
    #        'contextOut': req['result']['contexts']}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
