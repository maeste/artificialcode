"""Stream the default webcam to a web page via MJPEG over HTTP."""

import argparse
import signal
import sys
import threading
import time
from typing import Optional

import cv2
from flask import Flask, Response


app = Flask(__name__)

_camera_lock = threading.Lock()
_latest_frame: Optional[bytes] = None
_stop_event = threading.Event()


def capture_loop(device: int, width: int, height: int, fps: int, jpeg_quality: int) -> None:
    global _latest_frame

    cap = cv2.VideoCapture(device)
    if not cap.isOpened():
        print(f"Could not open camera device {device}", file=sys.stderr)
        _stop_event.set()
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)

    encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality]
    frame_interval = 1.0 / max(fps, 1)

    try:
        while not _stop_event.is_set():
            tick = time.monotonic()
            ok, frame = cap.read()
            if not ok:
                time.sleep(0.01)
                continue

            ok, buf = cv2.imencode(".jpg", frame, encode_params)
            if not ok:
                continue

            with _camera_lock:
                _latest_frame = buf.tobytes()

            elapsed = time.monotonic() - tick
            if elapsed < frame_interval:
                time.sleep(frame_interval - elapsed)
    finally:
        cap.release()


def mjpeg_generator():
    boundary = b"--frame"
    while not _stop_event.is_set():
        with _camera_lock:
            frame = _latest_frame
        if frame is None:
            time.sleep(0.05)
            continue
        yield boundary + b"\r\n"
        yield b"Content-Type: image/jpeg\r\n"
        yield f"Content-Length: {len(frame)}\r\n\r\n".encode("ascii")
        yield frame
        yield b"\r\n"


INDEX_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Webcam stream</title>
    <style>
      body { margin: 0; background: #111; color: #eee; font-family: system-ui, sans-serif; }
      header { padding: 12px 16px; border-bottom: 1px solid #333; }
      main { display: flex; justify-content: center; align-items: center; padding: 16px; }
      img { max-width: 100%; height: auto; border: 1px solid #333; }
    </style>
  </head>
  <body>
    <header><strong>Webcam stream</strong> (MJPEG)</header>
    <main><img src="/stream" alt="Live webcam stream"></main>
  </body>
</html>
"""


@app.route("/")
def index() -> str:
    return INDEX_HTML


@app.route("/stream")
def stream() -> Response:
    return Response(
        mjpeg_generator(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


def handle_sigterm(_signum, _frame):
    _stop_event.set()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=5000, help="Bind port (default: 5000)")
    parser.add_argument("--device", type=int, default=0, help="OpenCV camera index (default: 0)")
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--quality", type=int, default=80, help="JPEG quality 1-100")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, handle_sigterm)
    signal.signal(signal.SIGTERM, handle_sigterm)

    capture_thread = threading.Thread(
        target=capture_loop,
        args=(args.device, args.width, args.height, args.fps, args.quality),
        daemon=True,
    )
    capture_thread.start()

    # Give the camera a moment to warm up before serving.
    time.sleep(0.5)
    if _stop_event.is_set():
        return 1

    try:
        app.run(host=args.host, port=args.port, threaded=True, use_reloader=False)
    finally:
        _stop_event.set()
        capture_thread.join(timeout=2.0)

    return 0


if __name__ == "__main__":
    sys.exit(main())
