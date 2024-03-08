import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('Photos/sukuna_2.jpg')
# cv.imshow("Sukuna", img)

blank[:] = 0,255,0
cv.imshow("Green", blank)
cv.waitKey(0)
