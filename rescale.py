import cv2 as cv

#Fumctions for resizing
def rescaleFrame(frame, scale=0.75):#this works for both images and Videos
    #hieight[0]*width[1]
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):#fro live videos only
    capture.set(3,width)
    capture.set(4,height)


####resized images
img = cv.imread('E:\SELF DRIVING CAR\opencv-course-master\Resources\Photos\cat.jpg')
cv.imshow('Cat', img)

resized_img = rescaleFrame(img)
cv.imshow('ResizedImage', resized_img)

cv.waitKey(0)

###Reading And Resize Videos
capture = cv.VideoCapture('E:\SELF DRIVING CAR\opencv-course-master\Resources\Videos\dog.mp4')#u can refence using path, or 0 (for webcam), 1..(for the no. of diff cameras)
#capture = cv.VideoCapture(0)
while True:#to ccapture video frame by frame
    isTrue, frame = capture.read()

    #frame_resized = rescaleFrame(frame)
    frame_resized = changeRes(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20)& 0xFF==ord('d'):#to wait for 20milesec till 'd' is pressed
        break

capture.release()
cv.destroyAllWindows()
