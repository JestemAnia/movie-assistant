import json

class Response:
    def __init__(self, message):
        self.fulfillmentText = message


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
