import argparse
import json
import os
import random
import math
import threading
import time

class Synth:
    def __init__(self):
        self.freqs = [random.uniform(1, 50) for _ in range(5)]
        self.phases = [random.uniform(0, 2 * math.pi) for _ in range(5)]
        self.state_vars = [0] * 10
        self.sampling_rate = 256
        self.running = False


    def generate_and_save_data_old2(self):
        t = 0
        while self.running:
            for _ in range(self.sampling_rate):
                eeg_data = {
                    "ch1": sum([math.sin(2 * math.pi * f * t + p) for f, p in zip(self.freqs, self.phases)]),
                    "ch2": 0,
                    "ch3": 0,
                    "ch4": 0,
                }
                t += 1 / self.sampling_rate

                with open('eeg_data.json', 'a') as outfile:
                    json.dump(eeg_data, outfile)
                    outfile.write('\n')

                time.sleep(1 / self.sampling_rate)

    def generate_and_save_data(self):
        t = 0
        while self.running:
            data_chunk = []
            for _ in range(self.sampling_rate):
                eeg_data = {
                    "ch1": math.sin(2 * math.pi * self.freqs[0] * t + self.phases[0]),
                    "ch2": math.sin(2 * math.pi * self.freqs[1] * t + self.phases[1]),
                    "ch3": math.sin(2 * math.pi * self.freqs[2] * t + self.phases[2]),
                    "ch4": math.sin(2 * math.pi * self.freqs[3] * t + self.phases[3]),
                }
                data_chunk.append(eeg_data)
                t += 1 / self.sampling_rate
                time.sleep(1 / self.sampling_rate)

            with open('eeg_data.json', 'a') as outfile:
                for data in data_chunk:
                    json.dump(data, outfile)
                    outfile.write('\n')

            time.sleep(1 / self.sampling_rate)



    def generate_and_save_data_old(self):
        t = 0
        while self.running:
            data_chunk = []
            for _ in range(self.sampling_rate):
                eeg_data = {
                    "ch1": sum([math.sin(2 * math.pi * f * t + p) for f, p in zip(self.freqs, self.phases)]),
                    "ch2": 0,
                    "ch3": 0,
                    "ch4": 0,
                }
                data_chunk.append(eeg_data)
                t += 1 / self.sampling_rate
                time.sleep(1 / self.sampling_rate)

            print("In generate_and_save_data")

            with open('eeg_data.json', 'a') as outfile:
                json.dump(data_chunk, outfile)
                json.dump(data_chunk, outfile)
                outfile.write('\n')

            time.sleep(1 / self.sampling_rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--synth", action="store_true",
            help="Use synth to generate data")
    args = parser.parse_args()

    if args.synth:
        synth = Synth()
        print("Synth state:")
        print("Frequencies:", synth.freqs)
        print("Phases:", synth.phases)

        synth.running = True
        synth_thread = threading.Thread(target=synth.generate_and_save_data)
        synth_thread.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("KeyboardInterrupt")

        if args.synth:
            synth.running = False
            synth_thread.join()

