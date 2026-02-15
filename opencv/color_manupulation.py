import cv2
import numpy as np

cap=cv2.VideoCapture("opencv/resource/vid.mp4")

while True:
    ret, frame =cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # converting to HSV color format

    # the following range of colors will be displayed
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask=cv2.inRange(hsv, lower_blue, upper_blue)
                    # the values of the arrays falling in this range are rendered while the out of range colors are actually set to zero
                    # mask are either 0 or 1

    result = cv2.bitwise_and(frame, frame, mask=mask)
                    # cv2.bitwise_and(source_frame, second_source image , mask ---> determine the blending thing...)

    # cv2.imshow("Frame", mask)
    cv2.imshow("Frame", result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

