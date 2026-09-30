# 🧠 NeuroBot — Mind-Controlled Robotic Arm
Youtube Link - https://youtu.be/TXFSgJyz0Ko
### PRISM GenAI Hackathon 2026

**NeuroBot** is an assistive Brain-Computer Interface (BCI) prototype that converts biosignal events into physical robotic-arm movements using **EEG, EMG, Python, LSL and Arduino**.

> **From biological intent to real-world movement.**

---

## 🎯 Problem Statement

People with severe motor impairments may find conventional interfaces such as joysticks, keyboards, switches and touch controls difficult or impossible to operate.

Existing EEG-based robotic systems can also face challenges such as noisy signals, false triggers, user fatigue and inconsistent control.

NeuroBot explores a more intuitive biosignal-driven interface for assistive robotic control.

---

## 💡 Our Solution

NeuroBot combines **EEG-based brain-signal acquisition** with an **EEG + EMG hybrid architecture** to create a real-time human-machine interaction system.

```text
EEG / EMG Biosignals
        ↓
Signal Acquisition
        ↓
Real-Time Processing
        ↓
Event Detection
        ↓
Python BCI Controller
        ↓
Movement Command
        ↓
Serial Communication
        ↓
Arduino
        ↓
Robotic Arm
```

The EEG signal is streamed to Python using **Lab Streaming Layer (LSL)**. Python continuously monitors the incoming signal and, when the configured event is detected, sends a movement command to the Arduino.

---

## ⚡ Key Features

- 🧠 Real-time EEG event detection
- 💪 Hybrid EEG + EMG architecture
- 🔄 Continuous biosignal monitoring
- 🌐 LSL-based EEG streaming
- ⚙️ Python-based signal processing
- 🔌 Python-to-Arduino serial communication
- 🤖 Physical robotic-arm actuation
- 🛡️ Cooldown mechanism to reduce repeated triggers
- 🧩 Modular and expandable architecture

### Robotic Commands

| Command | Action |
|---|---|
| `O` | Open Claw |
| `C` | Close Claw |
| `U` | Arm Up |
| `D` | Arm Down |

---

## 🌍 Impact

NeuroBot demonstrates how biosignals can provide an alternative interaction pathway for people with limited motor control.

Potential applications include:

- Assistive robotics
- Accessibility technology
- Rehabilitation research
- Hands-free device interaction
- Human-machine interfaces
- Brain-Computer Interface research

---

## 🧪 Demonstration

The prototype demonstrates the complete real-time pipeline:

```text
Live EEG
   ↓
LSL Stream
   ↓
Python Event Detection
   ↓
Movement Command
   ↓
Arduino
   ↓
Robotic Arm Response
```

### EEG Test

`test_eeg.py` checks whether EEG data is successfully reaching Python through LSL.

```bash
python test_eeg.py
```

### Complete System

`eeg_control.py` runs the complete EEG-to-robotic-arm control pipeline.

```bash
python eeg_control.py
```

---

# 🚀 Installation & How to Run

## 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Mind-Controlled-Robotic-Arm
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

The terminal should now show:

```text
(.venv)
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Required Python packages:

```text
pylsl
pyserial
```

## 4. Prepare EEG

1. Turn on the EEG headset.
2. Connect it to the EEG acquisition software.
3. Verify sensor/electrode contact.
4. Start EEG acquisition.
5. Start the EEG LSL stream.
6. Ensure the LSL stream type is `EEG`.

## 5. Prepare Arduino

1. Connect the Arduino.
2. Open `arduino/robotic_arm.ino`.
3. Upload the program using Arduino IDE.
4. Check the Arduino COM port.
5. Close Arduino Serial Monitor before running Python.

If required, update the serial port in `eeg_control.py`:

```python
SERIAL_PORT = "COM7"
```

Replace `COM7` with the actual port assigned to the Arduino.

---

# ✅ Code Verification & Testing

Before running the complete hardware prototype, the software can be checked step-by-step.

## Step 1 — Check Python

```bash
python --version
```

A Python version should be displayed.

Then verify pip:

```bash
pip --version
```

---

## Step 2 — Activate the Virtual Environment

On Windows:

```bash
.venv\Scripts\Activate.ps1
```

The terminal should display:

```text
(.venv)
```

---

## Step 3 — Install / Verify Dependencies

```bash
pip install -r requirements.txt
```

To verify the required libraries:

```bash
python -c "import pylsl; import serial; print('All Python libraries working')"
```

Expected output:

```text
All Python libraries working
```

If `pylsl` is missing:

```bash
pip install pylsl
```

If PySerial is missing:

```bash
pip install pyserial
```

---

## Step 4 — Check `test_eeg.py` for Syntax Errors

Run:

```bash
python -m py_compile test_eeg.py
```

If the command returns to the terminal without displaying an error, the file has passed Python syntax checking.

Example:

```text
(.venv) > python -m py_compile test_eeg.py
(.venv) >
```

✅ `test_eeg.py` syntax is valid.

---

## Step 5 — Check `eeg_control.py` for Syntax Errors

Run:

```bash
python -m py_compile eeg_control.py
```

Again, no output means Python found no syntax errors.

✅ `eeg_control.py` syntax is valid.

---

## Step 6 — Test EEG Connection

Start the EEG device and LSL streaming software first.

Then run:

```bash
python test_eeg.py
```

Expected successful output:

```text
NEUROBOT - EEG CONNECTION TEST

Searching for EEG LSL stream...

[SUCCESS] Connected to EEG stream!

Stream Name   : ...
Stream Type   : EEG
Channels      : ...
Sampling Rate : ...

Receiving 10 EEG samples...

Sample 1: [...]
Sample 2: [...]
Sample 3: [...]
...
```

This confirms:

```text
EEG Device
    ↓
EEG Software
    ↓
LSL
    ↓
Python
    ↓
EEG Samples
```

✅ EEG-to-Python communication is working.

### If You Get `No EEG Stream Found`

This does **not automatically mean the Python code is broken**.

Check:

- EEG device is powered on.
- EEG acquisition software is running.
- Headset is connected.
- LSL streaming has started.
- The published stream type is `EEG`.

Then run:

```bash
python test_eeg.py
```

again.

---

## Step 7 — Run the Complete Controller

After confirming EEG samples and connecting the Arduino:

```bash
python eeg_control.py
```

The program should:

1. Find the EEG stream.
2. Connect to the Arduino.
3. Continuously read EEG samples.
4. Calculate signal changes.
5. Detect configured EEG events.
6. Generate a movement command.
7. Send the command through serial communication.
8. Trigger robotic-arm movement.

Example terminal output:

```text
Connected to EEG stream
Arduino connected
System Ready

Raw: 125.4 | Spike: 8.2
Raw: 130.8 | Spike: 5.4

EEG EVENT DETECTED
Sending command: O
```

---

## Step 8 — Verify Complete Pipeline

The final integration should follow:

```text
EEG Headset
     ↓
EEG Acquisition Software
     ↓
LSL
     ↓
test_eeg.py
     ↓
EEG Verified
     ↓
eeg_control.py
     ↓
Event Detection
     ↓
O / C / U / D Command
     ↓
Serial Communication
     ↓
Arduino
     ↓
Motor Driver
     ↓
Robotic Arm Movement
```

### Recommended Testing Order

```text
1. Check Python
        ↓
2. Install dependencies
        ↓
3. Compile-check test_eeg.py
        ↓
4. Compile-check eeg_control.py
        ↓
5. Test Python imports
        ↓
6. Start EEG + LSL
        ↓
7. Run test_eeg.py
        ↓
8. Confirm EEG samples
        ↓
9. Connect Arduino
        ↓
10. Run eeg_control.py
        ↓
11. Verify robotic-arm movement
```

---

## 🛠️ Technology Stack

**Software:** Python • pylsl • Lab Streaming Layer • PySerial • Arduino IDE • VS Code

**Hardware:** EEG Device • EMG Sensor • Arduino • Motor Driver • Robotic Arm • DC Motors

---

## 🔮 Future Scope

- Multi-channel EEG processing
- EEG + EMG sensor fusion
- Adaptive signal thresholds
- Machine-learning based intent classification
- Personalized user calibration
- Additional robotic-arm movements
- Force and position feedback
- Enhanced false-trigger prevention

---

## ⚠️ Prototype Note

NeuroBot is currently a **hackathon/research prototype** and not a certified medical device.

The current implementation uses EEG event detection to trigger robotic commands. Future versions can extend the system toward multi-command intent classification and deeper EEG-EMG fusion.

---

## 🏁 Conclusion

NeuroBot demonstrates a complete connection between **human biosignals and physical robotic action**.

By combining **EEG/EMG sensing, real-time Python processing, LSL streaming and Arduino-based robotic control**, NeuroBot explores how assistive systems can move beyond conventional physical controllers.

### **Think. Detect. Move. — NeuroBot**
