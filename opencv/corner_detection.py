import cv2
import numpy as np
import random as r

img = cv2.imread("opencv/resource/chess.jpg")
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
N=100

corners = cv2.goodFeaturesToTrack(gray, N, 0.01, 10)
                    # cv2.goodFeaturesToTrack(source_image, no_of_corners, minimum_quality, maximum_euclidean_distance ---> for rounded corners😁)
                    # coners matrix is actually floating point ---> convert it tnto integer matrix

corners = corners.astype(int)

for corner in corners:
    corner=corner[0]        # flatttening the array [[1,2,3,4]] ---> [1,2,3,4]
    cv2.circle(img, tuple(corner), 5, (0,0,255), -1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):

        point1=tuple(corners[i][0])
        point2=tuple(corners[j][0])
        a=r.randint(0,255)
        b=r.randint(0,255)
        c=r.randint(0,255)
        cv2.line(img,point1,point2, (a,b,c), 1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

