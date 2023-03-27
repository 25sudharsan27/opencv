import cv2 as cv
cam=cv.VideoCapture(0)

while True:
    isTrue,frame=cam.read()
    # cv.imshow('frame',frame)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # cv.imshow('framg',gray)



    haar_cascade=cv.CascadeClassifier('opencv-course/Section #3 - Faces/haar_face.xml')
    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('detect',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cam.release()
cv.destroyAllWindows()