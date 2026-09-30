# NeuroBot
## Mind-Controlled Assistive Robotic Arm using EEG & EMG

### PRISM GenAI Hackathon 2026

 **Prototype Demo:** [Watch on YouTube](https://youtu.be/TXFSgJyz0Ko)

**NeuroBot** is a Brain-Computer Interface (BCI) based assistive robotic-arm prototype that transforms detected biosignal events into physical robotic movements using **EEG, EMG, Python, Lab Streaming Layer (LSL), serial communication, and Arduino**.

> ### Think. Detect. Move.
> **From biological intent to real-world robotic action.**

---

#  Problem Statement

People with severe motor impairments may have limited ability to interact with conventional control systems such as joysticks, keyboards, switches, and touch interfaces.

Brain-Computer Interfaces provide an alternative pathway for human-machine interaction, but practical EEG-based control systems face several challenges:

- EEG signals are weak and susceptible to noise and artifacts.
- False detections can result in unintended commands.
- Signal characteristics vary between users and sessions.
- Continuous interaction may contribute to user fatigue.
- Reliable real-time communication between biosignal processing and physical hardware is required.
- Depending on a single biosignal can limit robustness.

**NeuroBot explores a low-cost, modular and assistive biosignal-driven approach to robotic control.**

---

#  Our Solution

NeuroBot creates an end-to-end pathway between **human biosignals and robotic movement**.

The prototype acquires EEG signals, streams them into Python through **Lab Streaming Layer (LSL)**, detects configured signal events, generates robotic commands, and communicates those commands to an Arduino.

The Arduino then converts the received commands into physical robotic-arm movements.

```text
┌─────────────────────────────┐
│        HUMAN USER           │
│         EEG + EMG           │
└─────────────┬───────────────┘
              │
              ▼
      SIGNAL ACQUISITION
              │
              ▼
        LSL STREAMING
              │
              ▼
     REAL-TIME PROCESSING
              │
              ▼
       EVENT DETECTION
              │
              ▼
     PYTHON BCI CONTROLLER
              │
              ▼
       MOVEMENT COMMAND
              │
              ▼
    USB SERIAL COMMUNICATION
              │
              ▼
       ARDUINO CONTROLLER
              │
              ▼
         MOTOR CONTROL
              │
              ▼
        🤖 ROBOTIC ARM
```

The broader NeuroBot architecture incorporates **EMG as a complementary biosignal modality**, providing a foundation for hybrid EEG-EMG interaction and future confirmation/safety mechanisms.

---

# What Makes NeuroBot Different?

### Biosignal-Based Interaction
Explores interaction without relying entirely on conventional physical controllers.

### Real-Time Processing
EEG samples are continuously streamed and processed through Python.

###  Hybrid Architecture
EEG provides the primary BCI pathway while EMG provides a complementary modality for future multimodal control.

###  End-to-End Integration
Connects signal acquisition, software processing, serial communication and physical actuation in one pipeline.

###  Trigger Protection
A cooldown mechanism helps prevent repeated immediate activations from the same detected event.

###  Modular Design
Signal acquisition, testing, processing and hardware control are separated, making the prototype easier to test and extend.

---

#  Robotic Arm Commands

NeuroBot currently supports four basic robotic actions:

| Serial Command | Action |
|:---:|---|
| `O` |  Open Claw |
| `C` |  Close Claw |
| `U` | ⬆ Move Arm Up |
| `D` | ⬇ Move Arm Down |

The Python BCI controller generates these commands and sends them to the Arduino through serial communication.

---

# How NeuroBot Works

The working prototype follows this real-time pipeline:

```text
LIVE EEG
   │
   ▼
LSL STREAM
   │
   ▼
PYTHON
   │
   ▼
SIGNAL CHANGE ANALYSIS
   │
   ▼
EVENT DETECTION
   │
   ▼
COMMAND GENERATION
   │
   ▼
O / C / U / D
   │
   ▼
USB SERIAL
   │
   ▼
ARDUINO
   │
   ▼
MOTOR CONTROL
   │
   ▼
ROBOTIC MOVEMENT
```

The current prototype monitors incoming EEG samples and detects signal events using an experimental threshold-based mechanism.

When the configured event condition is satisfied, the controller advances through the robotic command sequence and sends the corresponding command to the Arduino.

---

#  Impact & Applications

NeuroBot demonstrates how biosignals can provide an alternative pathway for interacting with machines.

### Potential Applications

- Assistive technology
- Assistive robotic systems
-  Brain-Computer Interface research
- Rehabilitation research
-  Hands-free machine interaction
- Biosignal-controlled systems
- Human-robot interaction
- Neurotechnology experimentation

The long-term objective is to explore more accessible interfaces that can reduce dependence on conventional physical controllers.

---

# Prototype Demonstration

The prototype demonstration shows the complete journey:

```text
Biosignal
   ↓
EEG Acquisition
   ↓
Live Signal Stream
   ↓
Python Detection
   ↓
Arduino Command
   ↓
Physical Movement
```

### 🎬 Demo Video

▶️ **[Watch NeuroBot Prototype Demonstration](https://youtu.be/TXFSgJyz0Ko)**

The demonstration includes the real-time signal-processing and robotic-control workflow used by the prototype.

---

# 📁 Repository Structure

```text
Mind-Controlled-Robotic-Arm/
│
├── eeg_control.py
│   └── Main EEG event detection and robotic-arm controller
│
├── test_eeg.py
│   └── Tests LSL connectivity and incoming EEG samples
│
├── two_motor_function.ino
│   └── Arduino firmware for motor and robotic-arm control
│
├── requirements.txt
│   └── Required Python packages
│
├── LangAI3.0_AI_Disclosure.docx
│   └── Official GenAI usage disclosure
│
├── SRM_WalkinDeadlines_Submission.pdf
│   └── Final hackathon presentation
│
├── README.md
│   └── Project documentation and reproducible setup guide
│
└── .gitignore
    └── Excludes virtual environments and temporary files
```

---

#  Technology Stack

### Software

| Technology | Purpose |
|---|---|
| **Python** | Real-time BCI processing and control |
| **Lab Streaming Layer (LSL)** | Real-time EEG data streaming |
| **pylsl** | Python interface for receiving LSL streams |
| **PySerial** | Python-to-Arduino serial communication |
| **Arduino IDE** | Firmware development and upload |
| **Visual Studio Code** | Python development and testing |
| **Git & GitHub** | Version control and project submission |

### Hardware

- EEG acquisition device
- EEG electrodes
- EMG sensor
- Arduino
- Motor driver / motor-control circuitry
- Robotic-arm structure
- Motors / actuators
- USB serial connection
- External motor power supply

---

#  Arduino Firmware

The Arduino firmware is available in:

```text
two_motor_function.ino
```

The Arduino forms the **physical control layer** of NeuroBot.

Python sends single-character commands:

```text
'O' → Open
'C' → Close
'U' → Up
'D' → Down
```

The Arduino receives the serial command and executes the corresponding motor-control operation.

```text
Python
   │
   │  O / C / U / D
   ▼
USB Serial
   │
   ▼
Arduino
   │
   ▼
Motor Control
   │
   ▼
Robotic Arm
```

### Uploading the Firmware

1. Connect the Arduino through USB.
2. Open `two_motor_function.ino` in Arduino IDE.
3. Select the correct Arduino board.
4. Select the appropriate COM port.
5. Verify/compile the sketch.
6. Upload the firmware.
7. Close Arduino Serial Monitor before running the Python controller.

> The Serial Monitor should be closed while running `eeg_control.py` because both applications cannot normally use the same serial port simultaneously.

---

#  Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/rahulagarwal2735/Mind-Controlled-Robotic-Arm.git
cd Mind-Controlled-Robotic-Arm
```

---

## 2. Create a Python Virtual Environment

```bash
python -m venv .venv
```

### Windows Command Prompt

```bash
.venv\Scripts\activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Main Python dependencies:

```text
pylsl
pyserial
```

---

# 🧠 EEG & LSL Setup

Before running NeuroBot:

1. Connect and power on the EEG acquisition device.
2. Open the compatible EEG acquisition software.
3. Verify the EEG electrodes and incoming signals.
4. Start EEG acquisition.
5. Enable/start the LSL stream.
6. Ensure an LSL stream with type `EEG` is available.

The expected path is:

```text
EEG Headset
     ↓
Acquisition Software
     ↓
LSL Stream
     ↓
Python
```

---

#  Code Verification

The project can be tested step-by-step before running the complete hardware pipeline.

## Step 1 — Check Python

```bash
python --version
```

Then:

```bash
pip --version
```

---

## Step 2 — Verify Dependencies

```bash
python -c "import pylsl; import serial; print('All Python libraries working')"
```

Expected output:

```text
All Python libraries working
```


---

## Step 3 — Verify Python Syntax

Check the EEG testing program:

```bash
python -m py_compile test_eeg.py
```

Check the main BCI controller:

```bash
python -m py_compile eeg_control.py
```

If the terminal returns without an error, Python found no syntax errors.

---

#  Test EEG Connectivity

Before starting robotic control, verify that Python can receive EEG samples.

Run:

```bash
python test_eeg.py
```

The script searches for an LSL stream with:

```text
type = EEG
```

Example successful output:

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
```

This verifies:

```text
EEG DEVICE → LSL → PYTHON  ✅
```


# Configure Arduino Serial Port

Check the Arduino port in:

```text
Windows Device Manager
        ↓
Ports (COM & LPT)
```

For example:

```text
Arduino (COM7)
```

Set the corresponding port in `eeg_control.py`.

Example:

```python
SERIAL_PORT = "COM7"
```

If the Arduino appears as `COM5`, change it accordingly.

---

# ▶️ Run the Complete NeuroBot System

After:

- EEG hardware is connected
- EEG acquisition is running
- LSL streaming is active
- Arduino firmware is uploaded
- Robotic arm is powered
- Correct serial port is configured

run:

```bash
python eeg_control.py
```

Example terminal output:

```text
Looking for EEG stream...

Connected to EEG stream
Arduino connected
System Ready

Raw: 125.4 | Spike: 8.2
Raw: 130.8 | Spike: 5.4

EEG EVENT DETECTED
Sending command: O
```

The complete execution is:

```text
EEG
 ↓
LSL
 ↓
Python
 ↓
Event Detection
 ↓
Movement Command
 ↓
Serial
 ↓
Arduino
 ↓
Motor
 ↓
Robotic Arm
```

---

# 🧪 Recommended Testing Sequence

```text
01  Install Python
        ↓
02  Create Virtual Environment
        ↓
03  Install requirements.txt
        ↓
04  Verify Python Files
        ↓
05  Start EEG Acquisition
        ↓
06  Start LSL Stream
        ↓
07  Run test_eeg.py
        ↓
08  Verify EEG Samples
        ↓
09  Upload Arduino Firmware
        ↓
10  Connect Robotic Arm
        ↓
11  Run eeg_control.py
        ↓
12  Verify Physical Movement
```

---

#  Control & Safety Logic

The current EEG controller includes:

### Event Threshold

A configurable threshold is used to identify significant changes in the incoming signal.

### Cooldown

After an event is detected, a short cooldown prevents immediate repeated triggering.

### Serial Command Layer

Only predefined commands are transmitted to the Arduino:

```text
O / C / U / D
```

This keeps the software-to-hardware interface simple and predictable.

---

#  Future Scope

###  Advanced BCI

- Multi-channel EEG processing
- Signal filtering and artifact reduction
- Adaptive thresholds
- Automatic user calibration

###  AI-Based Intent Recognition

- EEG feature extraction
- Machine-learning classifiers
- Independent multi-command classification
- Personalized user models
- Confidence-based command generation

### Hybrid EEG + EMG

- EMG-based command confirmation
- EEG-EMG sensor fusion
- False-trigger reduction
- Multimodal control

###  Advanced Robotics

- Additional degrees of freedom
- Position feedback
- Force sensing
- Collision detection
- Emergency-stop mechanisms
- Closed-loop robotic control

---

#  Conclusion

**NeuroBot connects biological signals with physical robotic action.**

By integrating **EEG/EMG sensing, real-time LSL streaming, Python-based event detection, serial communication, Arduino and robotic actuation**, the prototype demonstrates an end-to-end pathway from biosignal acquisition to real-world movement.

The current prototype establishes the foundation for future intelligent, personalized and multimodal assistive robotic systems.

> ## 🧠 THINK → ⚡ DETECT → 🤖 MOVE
>
> **NeuroBot — Bridging Human Intent and Robotic Action**