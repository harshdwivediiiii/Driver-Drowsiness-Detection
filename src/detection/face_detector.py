"""OpenCV Haar Cascade ML Model based face detection helpers."""

from typing import List, Tuple

import cv2


BoundingBox = Tuple[int, int, int, int]


def load_face_cascade() -> cv2.CascadeClassifier:
    """Load and validate frontal-face Haar Cascade."""
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    classifier = cv2.CascadeClassifier(cascade_path)
    if classifier.empty():
        raise FileNotFoundError("Could not load OpenCV face cascade.")
    return classifier


def detect_face(
    gray_frame,
    face_cascade: cv2.CascadeClassifier,
    scale_factor: float,
    min_neighbors: int,
    min_size: Tuple[int, int],
) -> List[BoundingBox]:
    """Detect faces in a grayscale frame."""
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=min_size,
    )
    return list(faces)
