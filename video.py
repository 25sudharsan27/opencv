# How to read a video
# capture=cv.VideoCapture(0)
#
# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('frame',frame)
#     if cv.waitKey(20) & 0xFF==ord('w'):
#         break
#
# capture.release()
# capture.destroyAllWindows()

import cv2 as cv

# img=cv.imread('photos/IMG_20230319_140103.jpg')
#
# cv.imshoww('Sudharsan',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize (frame,dimensions, interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('video1.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllwindows()