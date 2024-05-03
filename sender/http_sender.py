import requests

from . import sender

class HTTPMidiSender(sender.MidiSender):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def send_message(self, midi):
        data = self.parse_data(midi)
        requests.post(self.endpoint, json=data)
