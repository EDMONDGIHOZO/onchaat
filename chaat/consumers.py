import json
from channels.generic.websocket import WebsocketConsumer


class ChaatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.load(text_data)
        message = text_data_json['message']

        self.send(text_data_json.dumps({
            'message': message
        }))
