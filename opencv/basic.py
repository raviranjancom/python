import cv2

img = cv2.imread("C:/Users/Ravi/Documents/codes/python/opencv/resource/image.png", 1)    
                # for reading image ----> imread(path, mode)
                # mode --> defauld mode is BGR format

                # -1, cv2.IMREAD_COLOR : Any transparency of image will be neglacted. It is a default flag
                # 0, cv2.IMREAD_GRAYSCALE : Laod image in grayscale mode
                # 1, cv2.IMREAD_UNCHANGED : Load image as such including alpha channel
# img= cv2.resize(myimg, (400, 400))      # cv2.resize(myimg, (0, 0), fx=0.5, fy=0.5)
img =cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img=cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('resource/new_img.jpg', img)


cv2.imshow('myimage',img)
cv2.waitKey(0)      # wait for t time for key presses cv2.waitKey(t), if not zero it will wait for t seconds and for 0 time is infinite
cv2.destroyAllWindows() 
