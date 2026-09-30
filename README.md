# Mind-Controlled Robotic Arm Using EEG and EMG

## PRISM GenAI Hackathon 2026

A hybrid Brain-Computer Interface (BCI) based assistive robotic arm designed to translate human intent into physical robotic movement using EEG and EMG biosignals.

---

## Problem Statement

People with severe motor impairments may have limited ability to interact with conventional assistive devices such as joysticks, switches, or controllers.

Existing EEG-based robotic control systems can also suffer from noisy signals, false detections, user fatigue, and inconsistent control.

Our project explores a hybrid EEG-EMG approach for more reliable and intuitive robotic arm control.

---

## Proposed Solution

The system combines:

- EEG-based brain signal acquisition
- EMG-based muscle signal acquisition
- Real-time biosignal processing
- Intent detection
- Python-based BCI control
- Serial communication
- Arduino-based motor control
- Robotic arm actuation

The goal is to allow a user to generate control commands with minimal physical interaction.

---

## System Architecture

```text
EEG + EMG Signals
        |
        v
Signal Acquisition
        |
        v
Preprocessing
        |
        v
Intent Detection
        |
        v
Python BCI Controller
        |
        v
Serial Communication
        |
        v
Arduino Controller
        |
        v
Robotic Arm


Key Features
- EEG-based intent detection
- EMG-assisted control architecture
- Real-time biosignal processing
- LSL-based EEG data streaming
- Python signal processing
- Arduino serial communication
- Robotic arm movement control
- Modular hardware/software architecture
- Designed for assistive applications
Why Hybrid EEG + EMG?
EEG provides information related to brain activity but can be sensitive to noise and artifacts.
EMG provides information from residual muscle activity.
Combining multiple biosignal sources can support the development of a more robust control mechanism compared with relying on a single signal source.
Technology Stack
Software
- Python
- Lab Streaming Layer (LSL)
- pylsl
- NumPy
- PySerial
- Arduino IDE
- Visual Studio Code
Hardware
- EEG acquisition device
- EMG sensor
- Arduino
- Motor driver / motor shield
- Robotic arm
- DC motors / actuators
- External motor power supply