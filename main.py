import config
import rtmidi

from sender import udp_sender, http_sender


def print_message(midi):
    if midi.isNoteOn():
        # print('ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity())
        print('ON: ',midi.getNoteNumber(), midi.getVelocity(), midi.getChannel())

    # elif midi.isNoteOff():
    #     print('OFF:', midi.getMidiNoteName(midi.getNoteNumber()))
    # elif midi.isController():
    #     print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())

def main():
    if config.mode == "udp":
        sender = udp_sender.UDPMidiSender(config.udp_endpoint)
    elif config.mode == "http":
        sender = http_sender.HTTPMidiSender(config.http_endpoint)
    else:
        print(f"Invalid sender mode '{config.mode}'")
        return
        
    midiin = rtmidi.RtMidiIn()
    ports = range(midiin.getPortCount())
    print(f"{midiin.getPortCount()} in ports found")
    if ports:
        port = 0
        for i in ports:
            print(midiin.getPortName(i))
            if "loopMIDI" in midiin.getPortName(i):
                port = i
        print(f"Opening port {midiin.getPortName(port)}!") 
        midiin.openPort(port)
        while True:
            m = midiin.getMessage(5) # some timeout in ms
            if m:
                # print(m.getRawData())
                # print(type(m.midiChannelMetaEvent))
                # print(dir(m))
                # print(m.isMidiChannelMetaEvent())
                if m.isNoteOnOrOff():
                    sender.send_message(m)
                    print_message(m)
                # elif m.isMetaEvent():
                #     print(m)
    else:
        print('NO MIDI INPUT PORTS!')

if __name__ == "__main__":
    main()