import cv2
import numpy as np

img = cv2.imread("image/kingguin.jpg")
img = cv2.resize(img, (600,600))
HEIGHT, WIDTH = img.shape[:2]
pixel_h, pixel_w = (45,45)

tmp = cv2.resize(img, (pixel_w, pixel_h), interpolation= cv2.INTER_LINEAR)

output = cv2.resize(tmp, (WIDTH, HEIGHT), interpolation= cv2.INTER_NEAREST)

cv2.imshow("Input", img)
cv2.imshow("Output",output)

cv2.waitKey(0)