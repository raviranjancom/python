import numpy as np
import cv2

cap = cv2.VideoCapture("opencv/resource/vid.mp4")   # number of cameras as parameters like indexof array  ---> or add a video file path

while(True):
    ret, frame =cap.read()  # returns a frame as numpy image, and ret a boolean as if camerais accessable
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow('frame', frame)

    if (cv2.waitKey(1) == ord('q')):
        break;

cap.release()
cv2.destroyAllWindows()
