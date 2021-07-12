import cv2
import numpy as np
# Load the images or videos 
video=cv2.VideoCapture("green.mp4")
# video=cv2.VideoCapture(0)
#image of green color
image =cv2.imread("bg.jpeg")
while True:
    #read Video file ..
    ret, frame = video.read()
    #Resize the images and the videos to the same size
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    #Load the upper and lower BGR values of the green color
    u_green= np.array([104, 153, 70])
    l_green= np.array([30, 30, 0])
    #Apply the mask and then use bitwise and
    mask = cv2.inRange (frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    # Substract bitwise and from the original green screen image
    f = frame-res
    #Check for matrix value 8 after substraction and replace it by the second image
    f = np.where(f == 0, image, f)
    #Display The Video
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)
    if cv2.waitKey(25) == 27:
     break
video.release()

cv2.destroyAllWindows()