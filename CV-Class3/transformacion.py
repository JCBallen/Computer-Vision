import cv2 as cv
import numpy as np

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)

# cv.imshow('lol',img)
im2 = img.copy()
wid = img.shape[1]
hgt = img.shape[0]
# print(wid,hgt)


def negativo(img):
    global wid, hgt, im2
    for i in range(wid-1):
        for j in range(hgt-1):
            im2[i][j] = 255-img[i][j]
    return im2


def logaritmica(img, c):
    global wid, hgt, im2
    for i in range(wid):
        for j in range(hgt):
            im2[i][j] = c*np.log10(1+img[i][j])
    return im2


def potencia(img, c, gamma):
    global wid, hgt, im2
    for i in range(wid):
        for j in range(hgt):
            im2[i][j] = c*(img[i][j]**gamma)
    return im2


def intensidad(img, brillo):
    # global wid, hgt, im2
    for i in range(wid):
        for j in range(hgt):
            im2[i][j] = img[i][j]+brillo
    return im2


def contraste(img, i_min, i_max):
    for i in range(wid):
        for j in range(hgt):
            im2[i][j] = (img[i][j]-i_min)*255/(i_max-i_min)
    return im2


# Requests
# img2 = negativo(img)
# img2 = logaritmica(img,54)
# img2 = potencia(img, 5, 2)
# img2 = intensidad(img, -45)
img2 = contraste(img, 100, 250)


img2 = np.array(img2)
cv.imshow('lol', img2)

cv.waitKey(0)
