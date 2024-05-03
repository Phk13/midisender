
class MidiSender():

    @staticmethod
    def parse_data(midi):
        return {
            "note": midi.getNoteNumber(),
            "velocity": midi.getVelocity(),
            "on": midi.isNoteOn(),
            "channel": midi.getChannel(),
        }

    def send_message(midi):
        print("Unimplemented")
