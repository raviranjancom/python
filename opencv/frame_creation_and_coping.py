import numpy as np
import cv2

cap = cv2.VideoCapture("opencv/resource/vid.mp4")   # number of cameras as parameters like indexof array  ---> or add a video file path

while(True):
    ret, frame =cap.read()  # returns a frame as numpy image, and ret a boolean as if camerais accessable
    
    width=int(cap.get(3))   # to get width
    height=int(cap.get(4))  # to get height

    image=np.zeros(frame.shape,np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2]=smaller_frame
    image[height//2:height, :width//2]=smaller_frame
    image[:height//2, width//2:width]=smaller_frame
    image[height//2:height, width//2:width]=smaller_frame


    cv2.imshow('frame', image)

    if (cv2.waitKey(1) == ord('q')):
        break;

cap.release()
cv2.destroyAllWindows()
