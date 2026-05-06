"""Simple non-blocking alarm helper."""

import platform
from threading import Lock, Thread

import cv2


_alarm_lock = Lock()
_alarm_active = False


def _play_alarm_beep() -> None:
    global _alarm_active
    try:
        if platform.system().lower() == "windows":
            import winsound

            for _ in range(4):
                winsound.Beep(2200, 180)
        else:
            for _ in range(4):
                print("\a", end="", flush=True)
                cv2.waitKey(180)
    finally:
        with _alarm_lock:
            _alarm_active = False


def trigger_alert() -> None:
    """Play short alert sound without blocking the video loop."""
    global _alarm_active
    with _alarm_lock:
        if _alarm_active:
            return
        _alarm_active = True

    Thread(target=_play_alarm_beep, daemon=True).start()
