from pylsl import StreamInlet, resolve_byprop
import serial
import numpy as np
import time

arduino = serial.Serial('COM7', 9600)
time.sleep(2)

print("Looking for EEG stream...")
streams = resolve_byprop('type', 'EEG', timeout=5)

if not streams:
    print("No EEG stream found")
    arduino.close()
    raise SystemExit

inlet = StreamInlet(streams[0])
print("Connected to EEG stream")

THRESHOLD = 800
COOLDOWN = 2
WINDOW_SIZE = 5

buffer = []
last_trigger_time = 0
sequence = [b'O', b'D', b'C', b'U', b'D', b'O', b'U', b'C']
step = 0

print("System Ready")

try:
    while True:
        sample, timestamp = inlet.pull_sample(timeout=1)

        if sample is None:
            continue

        raw_value = sample[0]
        buffer.append(raw_value)

        if len(buffer) > WINDOW_SIZE:
            buffer.pop(0)

        signal = abs(buffer[-1] - buffer[-2]) if len(buffer) > 1 else 0
        print(f"Raw: {raw_value:.1f} | Spike: {signal:.1f}")

        current_time = time.time()

        if signal > THRESHOLD and current_time - last_trigger_time > COOLDOWN:
            print("CLENCH DETECTED")
            command = sequence[step]
            print("Sending command:", command)
            arduino.write(command)

            step = (step + 1) % len(sequence)
            last_trigger_time = current_time
            buffer.clear()

        time.sleep(0.05)
finally:
    arduino.close()