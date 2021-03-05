import cv2 as cv
import numpy as np

##creat a blank image
blank = np.zeros((500,500, 3), dtype='uint8')#(width, hieight, channels)
cv.imshow('Blank', blank)

#img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\cat.jpg')
#cv.imshow('Cat', img)


#### 1. Paint image a given colour
#blank[200:300, 300:400] = 0,255,0#green B:G:R
#cv.imshow('Green', blank)

#### 2. Draw a rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)#(img, pt1,pt2, color, thickness)
cv.rectangle(blank,(50,50), (450,450), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#### 3.DrawCircle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255),thickness=2)#(img, pt1,pt2,radius, color, thickness)
cv.imshow('Circle', blank)

#### 4 .Line
cv.line(blank, (50,50),(450,450), (255,0,0),thickness= 3)#diagonal line
cv.imshow('Line',blank)

cv.line(blank, (50,250),(450,250), (255,0,0),thickness= 3)#strightine at middle
cv.imshow('Line',blank)

#### 5.Write text
cv.putText(blank, 'Hello , am the King',(50,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)#(img, text, org, fontface, fontscale, colo, thickness)
cv.imshow('Text',blank)

cv.waitKey(0)
