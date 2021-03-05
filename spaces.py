import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

#plt.imshow(img)#this shows img in RGB
#plt.show()
##BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

##BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

##BGR to L*a*
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

##BGR to RGB
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)#this shows img in RGB
plt.show()

####all the other color spaces can convert back to BGR
##HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

###NOTE
##HSV can be converted to Lab but HSV has to be converted first to BGR than to Lab

cv.waitKey(0)
