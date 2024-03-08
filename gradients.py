import cv2 as cv
import numpy as np

img = cv.imread('Photos/sukuna_2.jpg')
cv.imshow("Sukuna", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplaction
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian", lap)

# Sobel
soblex = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobley = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(soblex, sobley)

cv.imshow('Sobel X', soblex)
cv.imshow('Sobel Y', sobley)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)



cv.waitKey(0)
