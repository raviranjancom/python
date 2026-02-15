import numpy as np
import cv2

cap = cv2.VideoCapture("opencv/resource/vid.mp4")   # number of cameras as parameters like indexof array  ---> or add a video file path

while(True):
    ret, frame =cap.read()  # returns a frame as numpy image, and ret a boolean as if camerais accessable
    
    width=int(cap.get(3))   # to get width
    height=int(cap.get(4))  # to get height

    # image=np.zeros(frame.shape,np.uint8)
    img=cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
    img=cv2.rectangle(frame, (100,100), (200,200) ,(0,0,255), 5)    # -1 == 5 to fill the rectangle
    img=cv2.circle(frame, (300,300), (100), (0,255,0), -1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame, "Mr. Robot", (10, height-10),font,4, (0,0,0),5,cv2.LINE_AA)

    cv2.imshow('frame', img)

    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
