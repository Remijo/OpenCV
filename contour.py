import cv2 as cv
import numpy as np

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

blank =np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur =cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


canny =cv.Canny(blur, 125,175)
cv.imshow('CannyEdge', canny)

###To filter img into pixels 0 and 1
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)#to work on intensite of pixels below(125) is set to binary zero, above(255) is set to binary one
#cv.imshow('Thresh', thresh)

###to draw n find contours on images

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_LIST--returns all contours in images
#RETR_EXTERNAL---returns all contours in outside of image
# RETR_TREE--returns all contours in in hierarchies in image
#cv.CHAIN_APPROX_NONE--how we want to approximate our image
#CHAIN_APPROX_SIMPLE--composses the image to only two points
print(f'{len(contours)} contours(s) found!')

###to show contours  on the image
cv.drawContours(blank, contours, -1, (0,0,255),2)#-1(rep both hozi n vertical drawnContours), 2(thickness)
cv.imshow('ContourDrawn', blank)

cv.waitKey(0)
