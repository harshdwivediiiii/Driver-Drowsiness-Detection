# Driver Drowsiness Detection System (OpenCV Only)

This is a real-time student project that detects driver drowsiness using a webcam and OpenCV Haar Cascades.

The project is fully refactored to remove `dlib`, facial landmarks, and heavy deep-learning dependencies.

## What This Project Does

- Detects face using OpenCV Haar Cascade
- Detects eyes inside detected face
- Uses simple logic:
  - if eyes are not detected for consecutive frames, treat eyes as closed
  - if eye-closure counter crosses threshold, mark driver as drowsy
- Triggers alert sound when drowsiness is detected
- Shows:
  - face and eye bounding boxes
  - system status (`ACTIVE` / `DROWSY`)
  - eye closure counter
  - FPS

## Why This Version Is Better

- Beginner-friendly code structure
- Easy to explain in interviews
- Lightweight setup (no model files, no dlib, no TensorFlow)
- Fast startup and minimal dependencies

## Project Structure

```text
Driver-Drowsiness-Detetction-System-main/
├── src/
│   ├── detection/
│   │   ├── face_detector.py
│   │   └── eye_detector.py
│   ├── utils/
│   │   ├── alarm.py
│   │   └── constants.py
│   └── main.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Press `q` to exit the camera window.

## How Drowsiness Is Detected

1. Convert webcam frame to grayscale
2. Detect face region
3. Detect eyes inside face region
4. If eyes are missing for many consecutive frames, increment closure counter
5. If closure counter exceeds threshold, show `DROWSY` and trigger alert

This avoids complex landmarks and still gives a practical drowsiness warning demo.

## Optional Note About `model_best.h5`

`model_best.h5` is not required in this OpenCV-only version.
You can keep it in the repository for reference, but it is not used in runtime.

## Author

Harshvardhan Dwivedi

## License

MIT License

