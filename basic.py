import cv2 as cv

img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\park.jpg')
cv.imshow('Cat', img)
#### Converting images to

# grayscale

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

#Blur
blur_img = cv.GaussianBlur(img ,(7,7), cv.BORDER_DEFAULT)#(3,3)is the kernl fro blurring img
cv.imshow('Blur',blur_img)

##Edge cascade

#canny =cv.Canny(img, 125, 175)# or use Dilating
canny =cv.Canny(blur_img, 125, 175)#to remove more of the edges or use Dilating
cv.imshow('CannyEdge',canny)

## Dilating the images
dilated = cv.dilate(canny, (3,3), iterations =3)
cv.imshow('DilatedImage', dilated)

## Eroding
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('Eroded', eroded)

##Resize or cropping images
resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)#interpolation r used incase u want to shiq or unlarge img omre tha original
cv.imshow('Resized',resized)

##cropping images
cropped = img[50:200, 200:400]
cv.imshow('Croped',cropped)

cv.waitKey(0)
