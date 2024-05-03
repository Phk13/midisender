import json
import socket

from . import sender

class UDPMidiSender(sender.MidiSender):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, midi):
        data = json.dumps(self.parse_data(midi))
        self._socket.sendto(data.encode(), self.endpoint)

    def close(self):
        self._socket.close()