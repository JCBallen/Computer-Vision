import cv2
import numpy as np

img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.imshow('result', dst)
cv2.waitKey(0)
