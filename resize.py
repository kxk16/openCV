import cv2 as cv

img = cv.imread('Photos/sukuna_2.jpg')

cv.imshow("Sukuna", img)

def rescaleFrame(frame, scale= 0.75):
# Works for everything
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img2 = rescaleFrame(img)
cv.imshow("resized_image", img2)
cv.waitKey(0)


capture = cv.VideoCapture('Videos/pexels.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break


def changeRes(width,height):
# Specifically for live videos
    capture.set(3,width)
    capture.set(4,height)

