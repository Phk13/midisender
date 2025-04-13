import struct


class MidiSender():

    @staticmethod
    def parse_data(midi):
        """
        Parse MIDI message into custom binary format.
        
        Format:
        1 byte: Note number (0-127)
        1 byte: Velocity (0-127)
        1 byte: Is note on (1 for on, 0 for off)
        1 byte: Channel (1-16)
        
        Args:
            midi: MIDI message object
            
        Returns:
            bytes: Custom binary representation of the MIDI message
        """
        return struct.pack('BBBB',
                         midi.getNoteNumber(),
                         midi.getVelocity(),
                         1 if midi.isNoteOn() else 0,
                         midi.getChannel())

    def send_message(midi):
        print("Unimplemented")