import cv2 as cv


capture=cv.VideoCapture(0)


def rescalframe(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


sssscale = float(input("Write which size you want: "))
while True:

    isTrue,frame=capture.read()
    cv.imshow('video',frame)

    reduced=rescalframe(frame,sssscale)
    cv.imshow('video shorted',reduced)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()