import cv2 as cv

img = cv.imread('Photos/sukuna_2.jpg')
cv.imshow('Sukuna',img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dialating the image
dialated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dialated', dialated)

# Eroding
eroded = cv.erode(dialated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500,500))
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0) 