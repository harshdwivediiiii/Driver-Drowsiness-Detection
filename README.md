<div align="center">

<h1>🚗 Driver Drowsiness Detection System</h1>

<p><strong>Real-time AI-powered driver fatigue monitoring using Computer Vision & OpenCV</strong></p>

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-1.24+-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/github/stars/harshdwivediiiii/Driver-Drowsiness-Detection?style=social" />
  <img src="https://img.shields.io/github/forks/harshdwivediiiii/Driver-Drowsiness-Detection?style=social" />
</p>

> **"AI for Safer Roads 🛣️"** — A lightweight, webcam-based fatigue detection system that triggers real-time alerts when a driver shows signs of drowsiness.

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [How It Works](#-how-it-works)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Key Features](#-key-features)
- [Dataset](#-dataset)
- [Getting Started](#-getting-started)
- [Output & Demo](#-output--demo)
- [Challenges & Learnings](#-challenges--learnings)
- [Roadmap](#-roadmap)
- [Contributors](#-contributors)
- [License](#-license)

---

## 📌 Overview

Driver fatigue is responsible for **over 20% of road accidents** globally. The **Driver Drowsiness Detection System** is a real-time computer vision solution built with Python and OpenCV that continuously monitors a driver's eye activity through a standard webcam.

When the system detects prolonged eye closure — a primary indicator of drowsiness — it immediately triggers a **visual warning** and **audio alarm** to wake the driver and prevent potential accidents.

Designed to be:
- 🪶 **Lightweight** — no dlib, no facial landmark predictors, no heavy ML pipelines
- ⚡ **Fast** — optimized for real-time performance on standard hardware
- 🎓 **Beginner-friendly** — clean modular code, perfect for learning CV fundamentals
- 💸 **Zero-cost** — runs on any webcam, no specialized hardware needed

---

## 🎯 Problem Statement

```
🚗 Every year, thousands of accidents occur due to driver fatigue.
💤 Drowsy driving impairs reaction time just as much as alcohol.
💰 Enterprise-grade safety systems remain inaccessible to most drivers.
```

This project demonstrates that an effective **early-warning fatigue detection system** can be built using only a webcam and open-source libraries — making road safety accessible to everyone.

---

## 🧠 How It Works

The system runs a continuous detection pipeline on each webcam frame:

```
┌─────────────────────────────────────────────────────────────┐
│                     DETECTION PIPELINE                      │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  1. CAPTURE  │  2. PREPROCESS  │  3. DETECT  │  4. ANALYZE  │
│              │                │             │               │
│  Webcam      │  Grayscale     │  Haar       │  Eye closure  │
│  frame grab  │  conversion    │  Cascade    │  frame count  │
│              │  + resize      │  face & eye │               │
└──────┬───────┴────────────────┴──────┬──────┴───────┬───────┘
       │                               │              │
       └───────────────────────────────┼──────────────┘
                                       ▼
                          ┌────────────────────────┐
                          │  Eyes closed > N frames?│
                          └────────┬───────┬────────┘
                                   │ YES   │ NO
                          ┌────────▼──┐  ┌─▼──────────────┐
                          │  🔔 ALERT │  │ Continue Normal │
                          │  Visual + │  │   Monitoring    │
                          │  Audio    │  └────────────────┘
                          └───────────┘
```

### Detection Logic

| State | Eyes Detected | Consecutive Closed Frames | Action |
|-------|--------------|--------------------------|--------|
| ✅ Alert | Both eyes open | 0 | No action |
| ⚠️ Caution | One eye closed | < threshold | Warning overlay |
| 🚨 Drowsy | Both eyes closed | ≥ threshold | Alarm triggered |

---

## 🏗️ System Architecture

```
Driver-Drowsiness-Detection/
├── src/
│   ├── detection/
│   │   ├── face_detector.py     ← Haar Cascade face detection
│   │   └── eye_detector.py      ← Eye region detection & analysis
│   │
│   ├── utils/
│   │   ├── alarm.py             ← Audio alert system (playsound)
│   │   └── constants.py         ← Thresholds, config values
│   │
│   └── main.py                  ← Pipeline orchestrator
│
├── main.py                      ← Entry point
├── train_model.ipynb            ← Research & model training notebook
├── model_best.h5                ← Trained model weights
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Technology | Version | Role |
|---|---|---|
| **Python** | 3.8+ | Core language |
| **OpenCV** | 4.x | Real-time video capture & CV |
| **NumPy** | 1.24+ | Numerical computation |
| **Haar Cascades** | Built-in | Face & eye detection |
| **Playsound** | 1.3.0 | Audio alarm playback |

### Why OpenCV-only?

Most drowsiness detection tutorials rely on `dlib` + facial landmark predictors, which adds:
- Heavy install size (~100MB+)
- C++ compilation requirements
- Complex setup on Windows

This project achieves the same goal with **zero heavy dependencies** — just `pip install` and run.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎥 **Real-time Monitoring** | Processes live webcam feed at target FPS |
| 👁️ **Eye Tracking** | Detects open/closed state per frame using Haar Cascades |
| 😴 **Drowsiness Detection** | Triggers alert after sustained eye closure beyond threshold |
| 🔔 **Dual Alert System** | On-screen warning overlay + audio alarm |
| 📊 **FPS Display** | Live performance counter on-screen |
| 🧩 **Modular Codebase** | Clean separation of detection, utils, and main logic |
| 🪶 **Lightweight** | No dlib, no heavy ML inference at runtime |
| 🖥️ **Cross-platform** | Works on Windows, macOS, Linux |

---

## 📊 Dataset

**[Kaggle Drowsiness Dataset](https://www.kaggle.com/datasets/dheerajperumandla/drowsiness-dataset)** by Dheeraj Perumandla

```
Dataset/
├── Open_Eyes/    ← Alert state images
├── Closed_Eyes/  ← Drowsy state images
└── Yawn/         ← Additional fatigue indicators
```

Used for: research, threshold calibration, and model training in `train_model.ipynb`. The Haar Cascade approach in `main.py` runs inference-free — no dataset required at runtime.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A working webcam
- `pip` package manager

### 1. Clone the Repository

```bash
git clone https://github.com/harshdwivediiiii/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
```

### 2. Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the System

```bash
python main.py
```

> Press **`Q`** to quit the webcam window.

---

### ⚠️ Troubleshooting

| Issue | Fix |
|---|---|
| Webcam not opening | Check that no other app is using the camera |
| `playsound` error on Linux | Install `gstreamer`: `sudo apt install python3-gst-1.0` |
| Low FPS | Reduce frame resolution in `constants.py` |
| Too many false positives | Increase `EYE_CLOSED_THRESHOLD` in `constants.py` |

---

## 🖥️ Output & Demo

When running, the system renders:

```
┌─────────────────────────────────────────┐
│  [LIVE WEBCAM FEED]                     │
│                                         │
│  ┌──────────────┐   FPS: 28             │
│  │  Face bbox   │   Status: ALERT ✅    │
│  │  ┌──┐  ┌──┐  │                      │
│  │  │L │  │R │  │   Eyes: OPEN          │
│  │  └──┘  └──┘  │                      │
│  └──────────────┘                       │
│                                         │
│  ⚠️  DROWSINESS DETECTED — WAKE UP!    │  ← triggers when drowsy
└─────────────────────────────────────────┘
```

On drowsiness detection:
- 🔴 Red warning banner overlaid on frame
- 🔔 Alarm sound plays immediately
- System resets counter once eyes reopen

---

## ⚠️ Challenges & Learnings

| Challenge | What We Learned |
|---|---|
| Lighting variations | Adaptive histogram equalization (CLAHE) for preprocessing |
| False positives on blinks | Threshold tuning — `N` consecutive frames vs single-frame detection |
| Webcam quality variance | Importance of resolution normalization before detection |
| Real-time performance | Frame skipping + ROI cropping to maintain target FPS |

These real-world constraints deepened understanding of production CV system design beyond textbook examples.

---

## 🔮 Roadmap

- [ ] **Deep Learning upgrade** — Replace Haar Cascades with MobileNet/EfficientNet eye classifier
- [ ] **EAR (Eye Aspect Ratio)** — More robust closure metric using MediaPipe Face Mesh
- [ ] **Head Pose Estimation** — Detect nodding/head drooping
- [ ] **Yawn Detection** — Additional fatigue indicator
- [ ] **Mobile App** — Android/iOS deployment via TFLite
- [ ] **Cloud Dashboard** — Fleet monitoring for commercial transport
- [ ] **Personalized Baselines** — Adaptive thresholds per driver profile
- [ ] **Smart Vehicle Integration** — CAN bus interface for embedded deployment

---

## 👨‍💻 Contributors

<table>
  <tr>
    <td align="center">
      <strong>Harshvardhan Dwivedi</strong><br/>
      <a href="https://github.com/harshdwivediiiii">@harshdwivediiiii</a>
    </td>
    <td align="center">
      <strong>Abhishek Kumar Yadav</strong><br/>
      CV Research & Integration
    </td>
    <td align="center">
      <strong>Rohit Pandey</strong><br/>
      Testing & Documentation
    </td>
  </tr>
</table>

**Department of CSE – AI/ML**
Rungta College of Engineering and Technology, Bhilai (CG)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [OpenCV Community](https://opencv.org/) — for the incredible open-source CV library
- [Dheeraj Perumandla](https://www.kaggle.com/datasets/dheerajperumandla/drowsiness-dataset) — for the Kaggle drowsiness dataset
- Kaggle community — for notebooks and research references

---

<div align="center">

**If this project helped you, drop a ⭐ — it keeps the momentum going!**

*Built with ❤️ for road safety and open-source learning*

</div>