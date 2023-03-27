import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype="uint8")
cv.imshow('bblank',blank)

def resizedas(frame,scale=0.5):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img=cv.imread('photos/photo.jpg')

resiz=resizedas(img,scale=0.1)
cv.imshow('cat',resiz)
cv.waitKey(0)