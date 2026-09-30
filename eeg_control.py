from pylsl import StreamInlet, resolve_byprop
import serial
import time

# =========================
# CONFIGURATION
# =========================
SERIAL_PORT = "COM7"   # Change according to Arduino COM port
BAUD_RATE = 9600

THRESHOLD = 800
COOLDOWN = 2
WINDOW_SIZE = 5

COMMAND_SEQUENCE = [
    b'O',  # Open
    b'D',  # Down
    b'C',  # Close
    b'U',  # Up
    b'D',
    b'O',
    b'U',
    b'C'
]

# =========================
# ARDUINO CONNECTION
# =========================
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)
    print(f"Arduino connected on {SERIAL_PORT}")
except serial.SerialException as e:
    print(f"Arduino connection failed: {e}")
    raise SystemExit

# =========================
# EEG CONNECTION
# =========================
print("Looking for EEG stream...")

streams = resolve_byprop(
    'type',
    'EEG',
    timeout=5
)

if not streams:
    print("No EEG stream found")
    arduino.close()
    raise SystemExit

inlet = StreamInlet(streams[0])

print("Connected to EEG stream")

# =========================
# EEG EVENT DETECTION
# =========================
buffer = []
last_trigger_time = 0
step = 0

print("System Ready")
print("Waiting for EEG events...")
print("Press CTRL+C to stop.")

try:

    while True:

        sample, timestamp = inlet.pull_sample(timeout=1)

        if sample is None:
            continue

        raw_value = sample[0]

        buffer.append(raw_value)

        if len(buffer) > WINDOW_SIZE:
            buffer.pop(0)

        if len(buffer) > 1:
            signal = abs(buffer[-1] - buffer[-2])
        else:
            signal = 0

        print(
            f"Raw: {raw_value:.1f} | "
            f"Spike: {signal:.1f}"
        )

        current_time = time.time()

        if (
            signal > THRESHOLD
            and current_time - last_trigger_time > COOLDOWN
        ):

            print("\nEEG EVENT DETECTED")

            command = COMMAND_SEQUENCE[step]

            print(
                "Sending command:",
                command.decode()
            )

            arduino.write(command)

            step = (
                step + 1
            ) % len(COMMAND_SEQUENCE)

            last_trigger_time = current_time

            buffer.clear()

        time.sleep(0.05)

except KeyboardInterrupt:

    print("\nSystem stopped.")

finally:

    arduino.close()
    print("Arduino connection closed.")