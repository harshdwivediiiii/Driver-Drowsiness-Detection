# Driver Drowsiness Detection System (OpenCV Only)

Driver Drowsiness Detection System is a lightweight, real-time webcam project that detects drowsiness with OpenCV Haar Cascades. It is intentionally simple and removes `dlib`, facial landmarks, and heavy deep-learning dependencies so it is easy to run, explain, and extend.

## Highlights

- Face detection with OpenCV Haar Cascades
- Eye detection inside the detected face region
- Simple frame-based drowsiness logic
- Alert sound when the driver appears drowsy
- On-screen status, counter, bounding boxes, and FPS

## How It Works

1. Capture a webcam frame and convert it to grayscale.
2. Detect the face region.
3. Detect eyes inside the face region.
4. If eyes are missing for several consecutive frames, treat them as closed.
5. If the closure counter crosses the threshold, show `DROWSY` and trigger the alert.

This keeps the project practical for a student demo while avoiding complex landmark pipelines.

## Project Structure

```text
Driver-Drowsiness-Detection/
├── main.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── detection/
│   │   ├── __init__.py
│   │   ├── face_detector.py
│   │   └── eye_detector.py
│   └── utils/
│       ├── __init__.py
│       ├── alarm.py
│       └── constants.py
├── model_best.h5
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8 or later
- Webcam access
- OpenCV installed from `requirements.txt`

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Press `q` to exit the camera window.

## Why This Version Is Better

- Beginner-friendly structure
- Fast startup with minimal dependencies
- Easy to present in interviews and classroom demos
- No required model downloads at runtime

## Optional Note About `model_best.h5`

`model_best.h5` is kept in the repository for reference only. It is not required for the OpenCV-only runtime path.

## Contributors

- Harshwardhan Dwivedi
- Abhishek Kumar Yadav
- Rohit Pandey

## License

MIT License

