import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/sukuna_2.jpg')
cv.imshow('Sukuna', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 200, 255, -1)

masked = cv.bitwise_and(img, img, mask= mask)
cv.imshow("Masked", masked)

cv.waitKey(0)


# For Grayscale Image

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.plot(gray_hist)
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.title('Grayscale Histogram')
# plt.xlim([0,255])
# plt.show()


# For Coloured Images

colours = ('b', 'g', 'r')
plt.figure()
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.title('Colour Histogram')

for i,col in enumerate(colours):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color= col)
    plt.xlim([0,256])

plt.show()

