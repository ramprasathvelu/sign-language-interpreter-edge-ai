# Real-Time Sign Language Interpreter using Computer Vision and Edge AI on Raspberry Pi
Real-time sign language recognition system using MediaPipe and Machine Learning, deployed on Raspberry Pi as an Edge AI solution. Converts hand gestures into text with optional speech output using a lightweight, low-cost architecture.
# 🤟 Real-Time Sign Language Interpreter — Edge AI on Raspberry Pi

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Raspberry%20Pi%204-red?style=for-the-badge&logo=raspberry-pi" />
  <img src="https://img.shields.io/badge/Framework-MediaPipe-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ML-Random%20Forest-green?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Deployment-Edge%20AI-orange?style=for-the-badge" />
</p>

> A real-time, GPU-free sign language recognition system that converts hand gestures into text and speech using MediaPipe hand landmark extraction, a custom-trained Machine Learning classifier, and majority voting for stable inference — deployed entirely on Raspberry Pi 4.

---

## 📌 Project Overview

Communication barriers faced by the deaf and hard-of-hearing community remain a significant challenge in everyday interaction. This project addresses that gap with a **low-cost, offline, edge-deployed sign language interpreter** that requires no internet connection, no GPU, and costs under ₹8,000 in hardware.

The system captures hand gestures from a camera, extracts 21 hand landmarks (63 numerical features) using Google MediaPipe, classifies the gesture using a trained Random Forest model, and outputs both **on-screen text** and **spoken audio** in real time.

Two deployment targets are supported:
- 💻 **PC / Laptop** — via webcam (for development and testing)
- 🍓 **Raspberry Pi 4** — full edge deployment (production target)

---

## ✋ Recognized Gestures (Custom Dataset)

| Gesture | Meaning |
|---|---|
| ✋ HELLO | Greeting |
| 👍 YES | Affirmation |
| 👎 NO | Negation |
| 🙏 THANK YOU | Gratitude |
| 🆘 HELP | Request for assistance |

> All gesture data was **collected and labeled manually** using the custom `collect_data.py` script — no pre-existing dataset was used.

---

## 🏗️ System Architecture

```
Camera Input
    │
    ▼
MediaPipe Hand Tracking
(21 landmarks → 63 XYZ features)
    │
    ▼
Random Forest Classifier
(trained on custom dataset.csv)
    │
    ▼
Majority Voting Buffer
(stabilizes flickering predictions)
    │
    ▼
┌──────────────┬──────────────┐
│  Text Output │ Speech Output│
│  (OpenCV UI) │ (gTTS/pyttsx3│
└──────────────┴──────────────┘
```

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Hand Tracking | MediaPipe (21 landmarks, 63 features) |
| ML Model | Scikit-learn Random Forest Classifier |
| Computer Vision | OpenCV |
| Text-to-Speech | gTTS / pyttsx3 |
| Video Streaming | Flask (stream server) |
| Data Handling | Pandas, NumPy |
| Edge Hardware | Raspberry Pi 4 (4GB / 8GB RAM) |
| Language | Python 3.9+ |

---

## 📂 Project Structure

```
sign-language-interpreter-edge-ai/
│
├── pc_webcam_code/               # PC/laptop development version
│   ├── collect_data.py           # Capture and label gesture data
│   ├── train_model.py            # Train Random Forest on dataset
│   ├── predict_stable.py         # Real-time inference with majority voting
│   ├── tts_engine.py             # Text-to-speech module
│   ├── stream_server.py          # Flask-based video streaming server
│   ├── dataset.csv               # Custom collected gesture dataset
│   └── model.pkl                 # Trained and serialized ML model
│
├── raspberry_pi_code/            # Raspberry Pi edge deployment version
│   ├── collect_data.py
│   ├── train_model.py
│   ├── predict_stable.py
│   ├── tts_engine.py
│   ├── stream_server.py
│   ├── dataset.csv
│   └── model.pkl
│
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works — Step by Step

**Step 1 — Data Collection**
Run `collect_data.py`, perform each gesture in front of the webcam, and press the label key. MediaPipe extracts 21 hand landmarks (x, y, z) → 63 features per frame → saved to `dataset.csv`.

**Step 2 — Model Training**
Run `train_model.py`. The script reads `dataset.csv`, splits into train/test sets, trains a Random Forest classifier, evaluates accuracy, and saves the model as `model.pkl`.

**Step 3 — Real-Time Inference**
Run `predict_stable.py`. Each video frame is processed by MediaPipe → features extracted → passed to the loaded model → raw prediction enters a majority voting buffer → stable gesture label is displayed on screen and optionally spoken aloud.

---

## 🖥️ Installation & Setup

### Prerequisites

- Python 3.9+
- Webcam (PC) or Pi Camera / USB cam (Raspberry Pi)
- Raspberry Pi 4 with Raspberry Pi OS (Bullseye or Bookworm)

### Clone the Repository

```bash
git clone https://github.com/ramprasathvelu/sign-language-interpreter-edge-ai.git
cd sign-language-interpreter-edge-ai
```

### Install Dependencies

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

**Key packages:**
```
opencv-python
mediapipe
scikit-learn
pandas
numpy
gTTS
pyttsx3
flask
```

---

## ▶️ Running the Project

### 1. Collect Your Own Gesture Data
```bash
cd pc_webcam_code        # or raspberry_pi_code
python collect_data.py
```
Follow the on-screen instructions to capture gesture samples.

### 2. Train the Model
```bash
python train_model.py
```
Outputs: `model.pkl` + accuracy report in the terminal.

### 3. Run Real-Time Detection
```bash
python predict_stable.py
```
A window opens showing live camera feed with gesture label overlay and spoken output.

### 4. (Optional) Stream via Flask
```bash
python stream_server.py
```
Access the stream at `http://<your-pi-ip>:5000` from any browser on the same network.

---

## 📊 Dataset Details

| Property | Value |
|---|---|
| Collection method | Custom — manually captured |
| Gesture classes | 5 (HELLO, YES, NO, THANK YOU, HELP) |
| Features per sample | 63 (21 landmarks × x, y, z) |
| Format | CSV |
| Extendable | Yes — run `collect_data.py` to add more gestures |

---

## 🔊 Output Example

```
GESTURE DETECTED: HELLO     → 🔊 "Hello"
GESTURE DETECTED: THANK YOU → 🔊 "Thank you"
GESTURE DETECTED: HELP      → 🔊 "Help"
GESTURE DETECTED: YES       → 🔊 "Yes"
GESTURE DETECTED: NO        → 🔊 "No"
```

---

## 💡 Applications

- Assistive communication devices for the deaf and hard-of-hearing
- Human-computer interaction without touch
- Edge AI / IoT proof-of-concept deployments
- Smart accessibility kiosks
- Real-time gesture control interfaces

---

## 📈 Future Improvements

- [ ] Expand to full ISL (Indian Sign Language) alphabet
- [ ] Two-hand simultaneous gesture recognition
- [ ] LSTM/CNN upgrade for temporal gesture sequences
- [ ] Mobile deployment (Android via TFLite)
- [ ] Sentence construction from sequential gestures
- [ ] Offline multilingual TTS (Tamil, Hindi)

---

## 🏆 Project Highlights

| Feature | Detail |
|---|---|
| No GPU required | Runs entirely on Raspberry Pi 4 CPU |
| No internet required | Fully offline after setup |
| Custom dataset | All gesture data collected from scratch |
| Dual deployment | Supports both PC and Raspberry Pi |
| Stable output | Majority voting eliminates prediction flicker |
| Low BOM cost | Hardware under ₹8,000 |

---

## 📜 License

This project is developed for academic and research purposes.
Feel free to use, fork, and extend with attribution.
