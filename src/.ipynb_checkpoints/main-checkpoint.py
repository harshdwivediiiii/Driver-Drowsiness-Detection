"""Main runtime for OpenCV-only driver drowsiness detection."""

import time

import cv2

from src.detection.eye_detector import calculate_eye_closure, detect_eyes, load_eye_cascade
from src.detection.face_detector import detect_face, load_face_cascade
from src.utils.alarm import trigger_alert
from src.utils.constants import (
    ALERT_RESET_FRAMES,
    CONSECUTIVE_CLOSED_EYE_FRAMES,
    EYE_MIN_NEIGHBORS,
    EYE_MIN_SIZE,
    EYE_SCALE_FACTOR,
    FACE_MIN_NEIGHBORS,
    FACE_MIN_SIZE,
    FACE_SCALE_FACTOR,
    WINDOW_NAME,
)


def draw_hud(frame, status: str, closure_counter: int, fps: float) -> None:
    """Draw status, eye-closure count and FPS on frame."""
    color = (0, 200, 0) if status == "ACTIVE" else (0, 0, 255)
    cv2.rectangle(frame, (10, 10), (370, 120), (20, 20, 20), -1)
    cv2.putText(frame, f"Status: {status}", (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    cv2.putText(
        frame,
        f"Eye Closure Counter: {closure_counter}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


def run() -> None:
    """Capture webcam frames and detect drowsiness using Haar cascades."""
    face_cascade = load_face_cascade()
    eye_cascade = load_eye_cascade()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam. Check camera permissions and availability.")

    closed_eye_frames = 0
    open_eye_stability_frames = 0
    prev_time = time.time()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.resize(frame, (960, 600))
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detect_face(
            gray_frame,
            face_cascade,
            scale_factor=FACE_SCALE_FACTOR,
            min_neighbors=FACE_MIN_NEIGHBORS,
            min_size=FACE_MIN_SIZE,
        )

        any_eyes_open = False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 140, 0), 2)
            face_gray = gray_frame[y : y + h, x : x + w]

            eye_boxes = detect_eyes(
                face_gray,
                eye_cascade,
                scale_factor=EYE_SCALE_FACTOR,
                min_neighbors=EYE_MIN_NEIGHBORS,
                min_size=EYE_MIN_SIZE,
            )

            for (ex, ey, ew, eh) in eye_boxes:
                cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

            if not calculate_eye_closure(eye_boxes):
                any_eyes_open = True

        if any_eyes_open:
            open_eye_stability_frames += 1
            if open_eye_stability_frames >= ALERT_RESET_FRAMES:
                closed_eye_frames = 0
        else:
            open_eye_stability_frames = 0
            closed_eye_frames += 1

        is_drowsy = closed_eye_frames >= CONSECUTIVE_CLOSED_EYE_FRAMES
        status = "DROWSY" if is_drowsy else "ACTIVE"

        if is_drowsy:
            trigger_alert()

        now = time.time()
        fps = 1.0 / max(now - prev_time, 1e-6)
        prev_time = now

        draw_hud(frame, status, closed_eye_frames, fps)
        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
