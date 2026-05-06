"""OpenCV Haar Cascade based eye detection helpers."""

from typing import List, Tuple

import cv2


EyeBox = Tuple[int, int, int, int]


def load_eye_cascade() -> cv2.CascadeClassifier:
    """Load and validate Haar Cascade for eye detection."""
    cascade_path = cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
    classifier = cv2.CascadeClassifier(cascade_path)
    if classifier.empty():
        raise FileNotFoundError("Could not load OpenCV eye cascade.")
    return classifier


def detect_eyes(
    gray_face_roi,
    eye_cascade: cv2.CascadeClassifier,
    scale_factor: float,
    min_neighbors: int,
    min_size: Tuple[int, int],
) -> List[EyeBox]:
    """Detect eyes inside a face ROI."""
    eyes = eye_cascade.detectMultiScale(
        gray_face_roi,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size,
    )
    return list(eyes)


def calculate_eye_closure(eye_boxes: List[EyeBox], min_eyes_for_open_state: int = 1) -> bool:
    """
    Return True when eyes are considered closed.

    Rule: if detected eyes are less than the minimum required count, treat eyes as closed.
    """
    return len(eye_boxes) < min_eyes_for_open_state
