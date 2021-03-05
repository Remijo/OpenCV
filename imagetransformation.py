import cv2 as cv
import numpy as np

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\park.jpg')

cv.imshow('City', img)

##Transformation

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x--->left
# -y-->up
# X-->right
# y-->down

translated = translate(img, 100, -100 )
cv.imshow('TranslatedImg', translated)

#Rotaion
def rotate(img, angle, rotPoint=None):
    #None is about center
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotatedImg =rotate(img, -90)#(img, angle)
cv.imshow('RotatedImage', rotatedImg)

# Resizing
resized = cv.resize(img, (500,500), interpolation= cv .INTER_CUBIC)#CUBIC or LINER for enlarging img, AREA for sharqing
cv.imshow('Resized', resized)

#Flipping
flip =cv.flip(img, 0)#0(verticalll), 1 (hozirontall), -1 (both)
cv.imshow('Flip', flip)

#cropping
cropped = img[100:400, 100:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)
