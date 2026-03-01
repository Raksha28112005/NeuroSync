from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import cv2
import random
import threading

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stress_score = 0

def camera_loop():
    global stress_score
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            # Fake stress logic for prototype
            stress_score = random.randint(40, 90)
        else:
            stress_score = random.randint(10, 40)

threading.Thread(target=camera_loop, daemon=True).start()

@app.get("/stress")
def get_stress():
    return {"stress_score": stress_score}