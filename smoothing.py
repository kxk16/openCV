import cv2 as cv

img = cv.imread('Photos/sukuna_2.jpg')
cv.imshow('Sukuna', img)

# Averaging Blur
average = cv.blur(img, (3,3))
cv.imshow("Ang_Blur", average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median Blur
# especially used in noise reduction in deep projects
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)