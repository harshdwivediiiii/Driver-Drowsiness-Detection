# 🚗 Driver Drowsiness Detection System (OpenCV Only)

> Real-time AI-based Driver Safety System using Computer Vision & OpenCV

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

Driver Drowsiness Detection System is a lightweight real-time computer vision project developed using **Python** and **OpenCV** to detect driver fatigue through webcam monitoring.

The system analyzes the driver's face and eye region continuously. If the eyes remain closed for several consecutive frames, the system identifies the driver as drowsy and triggers an alert alarm.

This project was designed as a practical AI/ML student project focused on:

* Real-time safety monitoring
* Computer Vision fundamentals
* Lightweight implementation without heavy dependencies

---

# 🎯 Problem Statement

Driver fatigue is one of the major causes of road accidents worldwide.

### Why This Matters

* Drowsy driving reduces reaction time
* Fatigue affects judgment and awareness
* Existing solutions are often expensive
* Need for affordable and accessible AI safety systems

This project demonstrates how Computer Vision can help improve road safety using only a standard webcam and OpenCV.

---

# 💡 Solution Overview

The system performs:

* Real-time webcam monitoring
* Face detection
* Eye detection
* Eye closure analysis
* Drowsiness detection
* Audio alert triggering

The project is intentionally lightweight and removes:

* ❌ dlib
* ❌ facial landmark predictors
* ❌ heavy deep learning pipelines

This makes the system:

* Easier to run
* Beginner-friendly
* Faster to deploy
* Better for demonstrations and presentations

---

# 🧠 System Workflow

## Workflow Pipeline

1. Video Capture using Webcam
2. Frame Preprocessing
3. Face Detection using Haar Cascades
4. Eye Detection inside face region
5. Eye Closure Analysis
6. Drowsiness Detection
7. Alert Trigger

---

# 🏗️ System Architecture

```text
Webcam Input
      ↓
Frame Processing
      ↓
Face Detection
      ↓
Eye Detection
      ↓
Eye Closure Analysis
      ↓
Drowsiness Detection
      ↓
Alert System
```

---

# ⚙️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Core programming language |
| OpenCV        | Real-time computer vision |
| NumPy         | Numerical operations      |
| Haar Cascades | Face & eye detection      |
| Playsound     | Alarm triggering          |
| GitHub        | Version control           |

---

# 📂 Project Structure

```text
Driver-Drowsiness-Detection/
│
├── .ipynb_checkpoints/
│
├── src/
│   │
│   ├── .ipynb_checkpoints/
│   │
│   ├── __pycache__/
│   │   ├── __init__.cpython-312.pyc
│   │   └── main.cpython-312.pyc
│   │
│   ├── detection/
│   │   │
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── eye_detector.py
│   │   └── face_detector.py
│   │
│   ├── models/
│   │   │
│   │   ├── __pycache__/
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   │
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── alarm.py
│   │   └── constants.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── LICENSE
├── README.md
├── iphone-alarm-vs-android-alarm-128-ytshorts.savetube.me.mp3
├── main.py
├── model_best.h5
├── requirements.txt
└── train_model.ipynb
# ✨ Key Features

✅ Real-time webcam monitoring
✅ Face detection using Haar Cascades
✅ Eye tracking system
✅ Drowsiness alert system
✅ FPS display
✅ Lightweight architecture
✅ Beginner-friendly modular code structure

---

# 📊 Dataset Used

### Kaggle Drowsiness Dataset

Dataset Source:

https://www.kaggle.com/datasets/dheerajperumandla/drowsiness-dataset

Dataset includes:

* Open eye images
* Closed eye images
* Drowsy state samples

The dataset was used for understanding driver fatigue behavior and project research.

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/harshdwivediiiii/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python main.py
```

Press `q` to exit the webcam window.

---

# 🖥️ Output

The system displays:

* Face detection bounding boxes
* Eye detection rectangles
* Drowsiness status
* FPS counter
* Alert warning overlay

When drowsiness is detected:

* Screen warning appears
* Alarm sound is triggered

---

# ⚠️ Challenges Faced

* Lighting condition variations
* False positives during blinking
* Webcam quality limitations
* Real-time performance optimization

These challenges helped improve understanding of:

* Image preprocessing
* Real-time CV systems
* Detection threshold tuning

---

# 🔮 Future Improvements

* Deep learning-based detection
* Head pose estimation
* Mobile application integration
* Cloud monitoring dashboard
* Personalized fatigue scoring
* Smart vehicle integration

---

# 👨‍💻 Contributors

* Harshvardhan Dwivedi
* Abhishek Kumar Yadav
* Rohit Pandey

Department of CSE – AI / AIML
Rungta College of Engineering and Technology, Bhilai (CG)

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgement

Special thanks to:

* OpenCV Community
* Kaggle Dataset Contributors
* NotebookLM & Claude AI for research support

---

# ⭐ Conclusion

This project demonstrates how AI and Computer Vision can be applied to real-world safety systems.

The Driver Drowsiness Detection System provides:

* affordable monitoring
* real-time detection
* lightweight implementation
* practical AI/ML learning experience

> “AI for Safer Roads 🚘”
