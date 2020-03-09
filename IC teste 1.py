pip install opencv-python
import cv2
import numpy as np
cap = cv2.VideoCapture("eye_recording.flv")
while True:
    ret, frame = cap.read()
    if ret is False:
        break