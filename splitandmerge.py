import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\park.jpg')
cv.imshow('Cats', img)
##img shape (w, h , channels)

blank = np.zeros(img.shape[:2], dtype ='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('MergedImage', merged)

cv.waitKey(0)
