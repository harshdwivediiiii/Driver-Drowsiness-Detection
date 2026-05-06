"""Project constants for the OpenCV-only implementation."""

WINDOW_NAME = "Driver Drowsiness Detection (OpenCV)"

# Face detection params
FACE_SCALE_FACTOR = 1.2
FACE_MIN_NEIGHBORS = 5
FACE_MIN_SIZE = (120, 120)

# Eye detection params
EYE_SCALE_FACTOR = 1.1
EYE_MIN_NEIGHBORS = 6
EYE_MIN_SIZE = (20, 20)

# Drowsiness rules
CONSECUTIVE_CLOSED_EYE_FRAMES = 15
ALERT_RESET_FRAMES = 3
