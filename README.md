# Real-Time Sign Language Interpreter using Computer Vision and Edge AI on Raspberry Pi
Real-time sign language recognition system using MediaPipe and Machine Learning, deployed on Raspberry Pi as an Edge AI solution. Converts hand gestures into text with optional speech output using a lightweight, low-cost architecture.
# 🧠 Real-Time Sign Language Interpreter using Computer Vision and Edge AI on Raspberry Pi

## 📌 Project Overview

This project is a real-time **sign language recognition system** built using Computer Vision, Machine Learning, and Edge AI.  
It converts hand gestures captured from a camera into **text and speech output**, enabling natural human–computer interaction and assistive communication.

The system is designed to run efficiently on a **Raspberry Pi 4**, making it suitable for low-cost embedded AI applications.

---

## 🚀 Key Features

- 🖐️ Real-time hand gesture detection using MediaPipe
- 🤖 Machine learning model trained on custom gesture dataset
- 📊 Uses 21 hand landmarks (63 features) for classification
- ⚡ Lightweight Edge AI deployment (Raspberry Pi compatible)
- 📢 Converts gestures into text and speech output
- 📷 Supports webcam or IP camera streaming
- 🔄 Stable prediction using majority voting for smooth output

---

## 🏗️ System Architecture

Camera → MediaPipe Hand Tracking → Feature Extraction (63 values) → ML Model → Stable Prediction → Text Output → Speech Output

---

## 🧠 Tech Stack

- Python
- OpenCV
- MediaPipe
- Scikit-learn (Random Forest Classifier)
- Pandas, NumPy
- gTTS / pyttsx3 (Text-to-Speech)
- Flask (video streaming server)
- Raspberry Pi 4 (Edge Device)

---

## 📂 Project Structure
sign-language-project/
│
├── collect_data.py # Dataset collection script
├── dataset.csv # Custom gesture dataset
├── train_model.py # ML model training script
├── model.pkl # Trained model
├── predict_stable.py # Real-time inference system
├── tts_engine.py # Speech output module
├── stream_server.py # Camera streaming server
└── README.md


---

## 🎯 Gesture Classes

Example trained gestures:

- HELLO  
- YES  
- NO  
- THANK YOU  
- HELP  

---

## ⚙️ How It Works

1. Camera captures hand movement in real time  
2. MediaPipe extracts 21 hand landmarks  
3. Landmarks converted into 63 numerical features  
4. Machine learning model predicts gesture class  
5. Majority voting stabilizes output  
6. Text is optionally converted into speech output  

---

## 🖥️ Installation

```bash
git clone https://github.com/your-username/sign-language-interpreter-edge-ai.git
cd sign-language-interpreter-edge-ai

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
▶️ Run Project
Train Model
python train_model.py
Run Real-Time Detection
python predict_stable.py
🔊 Output Example
GESTURE: HELLO → Hello
GESTURE: THANK YOU → Thank you

💡 Applications
Assistive communication systems
Human-computer interaction
Edge AI and IoT deployments
Smart accessibility devices
Real-time gesture recognition systems
📈 Future Improvements
Support for full alphabet gesture set
Two-hand gesture recognition
Deep learning upgrade (LSTM/CNN)
Offline speech engine optimization
Mobile deployment
🏆 Project Highlights
Fully real-time system
Runs on low-cost Raspberry Pi hardware
No GPU required
Custom dataset creation included
Edge AI optimized architecture

📜 License
This project is developed for academic and research purposes.
