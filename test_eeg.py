from pylsl import StreamInlet, resolve_byprop

print("Looking for EEG stream...")
streams = resolve_byprop("type", "EEG", timeout=10)

if not streams:
    print("No EEG stream found")
    raise SystemExit

inlet = StreamInlet(streams[0])
print("Connected to EEG stream!")

for _ in range(10):
    sample, timestamp = inlet.pull_sample(timeout=2)
    print(sample)