import cv2 as cv


img=cv.imread("photos/photo1.png")


def resize(frame,scale=0.1):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
# converting to grayscale

imgo=resize(img)
# cv.imshow('ori',img)
# grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# imgg=resize(grey)
# cv.imshow('GRAY',grey)



#Blur
#
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

#

# Edge Cascode
canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)

#Dilating the image

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)

# Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroede',eroded)

# Resize
risized=cv.resize(img,(500,500))
cv.imshow('Resized',risized)

# Cropping
cropped=img[50:200, 200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)