import cv2 as cv

import numpy as np

blank=np.zeros((500,500),dtype='uint8')
cv.imshow('Blank',blank)
# img=cv.imread('photos/photo.jpg')
# cv.imshow('cat',img)
blank[:] = 0,255,0
cv.imshow('green',blank)

cv.waitKey(0)
