from pylsl import StreamInlet, resolve_byprop

print("=" * 50)
print("NEUROBOT - EEG CONNECTION TEST")
print("=" * 50)

print("\nSearching for EEG LSL stream...")

# Search for an LSL stream whose type is EEG
streams = resolve_byprop(
    "type",
    "EEG",
    timeout=10
)

if not streams:
    print("\n[ERROR] No EEG stream found.")
    print("Make sure the EEG device and LSL stream are running.")
    raise SystemExit

# Connect to the first available EEG stream
stream = streams[0]
inlet = StreamInlet(stream)

print("\n[SUCCESS] Connected to EEG stream!")

print("Stream Name   :", stream.name())
print("Stream Type   :", stream.type())
print("Channels      :", stream.channel_count())
print("Sampling Rate :", stream.nominal_srate())

print("\nReceiving 10 EEG samples...\n")

for i in range(10):

    sample, timestamp = inlet.pull_sample(timeout=2)

    if sample is None:
        print(f"Sample {i + 1}: No data received")
    else:
        print(
            f"Sample {i + 1}: "
            f"{sample}"
        )

print("\nEEG connection test completed.")