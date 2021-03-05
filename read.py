import cv2 as cv
####reading images
#img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\cat_large.jpg')

#cv.imshow('Cat', img)
#cv.waitKey(0)
###Reading Videos
capture = cv.VideoCapture('E:\SELF DRIVING CAR\opencv-course-master\Resources\Videos\dog.mp4')#u can refence using path, or 0 (for webcam), 1..(for the no. of diff cameras)

while True:#to ccapture video frame by frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20)& 0xFF==ord('d'):#to wait for 20milesec till 'd' is pressed
        break

capture.release()
cv.destroyAllWindows() 
