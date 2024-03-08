import cv2 as cv

capture = cv.VideoCapture('Videos/pexels.mp4')


while True:
    isTrue, frames = capture.read()
    cv.imshow("Video", frames)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()