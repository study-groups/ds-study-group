import argparse
import json
import os
from pythonosc import dispatcher, osc_server

data = []

def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    global data
    data.append({"ch1": ch1, "ch2": ch2, "ch3": ch3, "ch4": ch4})

def save_data():
    global data
    with open('eeg_data.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="0.0.0.0", help="The IP to listen on")
    parser.add_argument("--port", type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/eeg", eeg_handler, "EEG")

    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        save_data()

