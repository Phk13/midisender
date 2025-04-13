import unittest
import struct
from unittest.mock import patch, MagicMock
from sender.sender import MidiSender
from sender.udp_sender import UDPMidiSender

class TestMidiSender(unittest.TestCase):
    def test_parse_data_note_on(self):
        # Create mock MIDI message
        midi = MagicMock()
        midi.getNoteNumber.return_value = 60  # Middle C
        midi.getVelocity.return_value = 100
        midi.isNoteOn.return_value = True
        midi.getChannel.return_value = 1
        
        result = MidiSender.parse_data(midi)
        expected = struct.pack('BBBB', 60, 100, 1, 1)
        self.assertEqual(result, expected)

    def test_parse_data_note_off(self):
        midi = MagicMock()
        midi.getNoteNumber.return_value = 60
        midi.getVelocity.return_value = 0
        midi.isNoteOn.return_value = False
        midi.getChannel.return_value = 1
        
        result = MidiSender.parse_data(midi)
        expected = struct.pack('BBBB', 60, 0, 0, 1)
        self.assertEqual(result, expected)

    def test_parse_data_edge_cases(self):
        # Test note number boundaries
        midi = MagicMock()
        midi.getNoteNumber.return_value = 0
        midi.getVelocity.return_value = 127
        midi.isNoteOn.return_value = True
        midi.getChannel.return_value = 16
        
        result = MidiSender.parse_data(midi)
        expected = struct.pack('BBBB', 0, 127, 1, 16)
        self.assertEqual(result, expected)

class TestUDPMidiSender(unittest.TestCase):
    @patch('socket.socket')
    def setUp(self, mock_socket):
        self.mock_socket = mock_socket
        self.sender = UDPMidiSender("127.0.0.1:8080")

    def test_send_message(self):
        midi = MagicMock()
        midi.getNoteNumber.return_value = 60
        midi.getVelocity.return_value = 100
        midi.isNoteOn.return_value = True
        midi.getChannel.return_value = 1
        
        self.sender.send_message(midi)
        self.mock_socket.return_value.sendto.assert_called_once()

    def test_close(self):
        self.sender.close()
        self.mock_socket.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()