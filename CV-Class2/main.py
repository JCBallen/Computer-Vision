import cv2 
import numpy as np

testim=cv2.imread('lenna.png')

cv2.imshow('Titulo de la imagen',testim)
cv2.waitKey()

grises = cv2.cvtColor(testim, cv2.COLOR_RGB2GRAY)

cv2.imshow('hola',grises)
cv2.waitKey()

h, w, c = testim.shape


print('width:  ', w)
print('height: ', h)
print('channel:', c)
h, w = grises.shape
print('width:  ', w)
print('height: ', h)


b,g,r = testim[5, 5]


for i in range(h):
  for j in range(w):
     print(testim[i,j])
  print('\n')