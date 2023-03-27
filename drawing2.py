import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('blank',blank)
# blank[:]=0,255,0
# cv.imshow('blank2',blank)
# blank[:]=255,0,0
# cv.imshow('blank3',blank)
# blank[:]=0,0,255
# cv.imshow('blank4',blank)
# cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
# cv.imshow('rectangle',blank)
# blank[140:200,140:200]=0,0,255
# cv.imshow('green',blank)

# Draw a Rectangle

# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow("rectangle",blank)
#
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0))
# cv.imshow('rectangle',blank)
#
# cv.waitKey(0)

# Draw a circle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
# cv.imshow('rectangle',blank)
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=2)
# cv.imshow('circle',blank)


# Draw a line

# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=2)
# cv.imshow("line",blank)


# Write a words
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("words",blank)


cv.waitKey(0)
