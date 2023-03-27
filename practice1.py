import cv2 as cv

capture=cv.VideoCapture(0)


def resizevideo(frame,scale=0.7):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0]* scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
while True:

    isTrue,frame=capture.read()
    cv.imshow('video',frame)
    reduced=resizevideo(frame)
    cv.imshow('video1',reduced)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows