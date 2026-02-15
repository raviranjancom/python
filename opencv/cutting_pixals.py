import cv2
import random

path = "opencv/resource/img.png"
mode = -1

img = cv2.imread(path, mode)

if img is None:
    print("❌ Image not found or invalid path.")
    exit()

h, w = img.shape[:2]

# Select a random 100×100 region (adjust size dynamically if needed)
block_h = min(100, h // 4)
block_w = min(100, w // 4)

# Random source position
src_y = random.randint(0, h - block_h)
src_x = random.randint(0, w - block_w)

# Random destination position
dst_y = random.randint(0, h - block_h)
dst_x = random.randint(0, w - block_w)

# Copy the region
img[dst_y:dst_y + block_h, dst_x:dst_x + block_w] = img[src_y:src_y + block_h, src_x:src_x + block_w]

cv2.imshow('myimage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
