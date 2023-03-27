import cv2 as cv
import time
import numpy as np


wcam,hcam=640,400


cap=cv.VideoCapture(0)

cap.set(3,wcam)
cap.set(4,hcam)
ptime=0
while True:
    success, img=cap.read()

    img=detector.findHands(img)


    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,f'FPS:{int(fps)} ',(40,50),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv.imshow('img',img)
    if cv.waitKey(20)==ord('d'):
        break

cap.release()
cv.destroyAllWindows()