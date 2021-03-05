##thiS IS DONE INCASE O NOISE IN VIDEOS N IMAGES
## THIS IS DONE IN DIFF METHODS
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\park.jpg')
cv.imshow('Cats', img)

## 1-Averaging(it averages all pixels around a given kernel region)
average = cv.blur(img, (3,3))
cv.imshow('Averaged', average)

## 2-GaussianBlur
gas_blur =cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GaussianBlur', gas_blur)

## 3-Median Blur
median = cv.medianBlur(img,3 )
cv.imshow('Median', median)

## 4-Bilateral(Blur is applied even to edges of img)
bilateral = cv.bilateralFilter(img , 5, 45, 35)# img ,5 is diameter, 15 (sigma), 15 is the spacing of the 5dia circle
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)
