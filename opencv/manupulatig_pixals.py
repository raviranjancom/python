import cv2
import random

path="opencv/resource/image.png"
mode=1

img=cv2.imread(path,mode)

for i in range(100):
    for j in range(img.shape[1]):           # img.shape --->  (rows, cols, channals)
        img[i][j]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow('myimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
