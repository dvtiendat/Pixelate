import cv2
import numpy as np

img = cv2.imread("image/kingguin.jpg")
img = cv2.resize(img, (600, 600))
HEIGHT, WIDTH = img.shape[:2]
pixel_h, pixel_w = (15, 15)

rg_x, rg_y, r_width, r_height = 100, 100, 200, 200

output = img.copy()
partial = output[rg_y:rg_y+r_height, rg_x:rg_x+r_width]

tmp = cv2.resize(partial , (r_width//pixel_w, r_height//pixel_h), interpolation=cv2.INTER_LINEAR)
pixelated_rg = cv2.resize(tmp, (r_width, r_height), interpolation=cv2.INTER_NEAREST)

output[rg_y:rg_y+r_height, rg_x:rg_x+r_width] = pixelated_rg

cv2.imshow("Input", img)
cv2.imshow("Output", output)
cv2.waitKey(0)
