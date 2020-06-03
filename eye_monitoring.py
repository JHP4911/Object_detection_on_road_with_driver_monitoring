import cv2                                            # import libraries of python OpenCV
import winsound
title = 'car control'
cv2.namedWindow(title)                                # capture frames from a camera
video = cv2.VideoCapture(0)
frequency = 2500                                      # Set Frequency To 2500 Hertz
duration = 60                                         # Set Duration To 60 msec

if video.isOpened():                                  # check if video is opened
    rval, frame = video.read()                        # return the value as  video frame
else:
    rval = False                                      # else return 0

# Paths to haarcascade_frontalface_alt.xml and haarcascade_eye.xml files 
faceCascade = cv2.CascadeClassifier("C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_alt.xml") 
eye_cascade = cv2.CascadeClassifier('C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
font = cv2.FONT_HERSHEY_SIMPLEX                       # opencv font                                                     
thickness = 2                                         # Line thickness of 2 px 
while rval:                                           # infinite loop untill the return value is true
    cv2.imshow(title, frame)                          # Display an image and title in a window 
    rval, frame = video.read()                        # reads frames from a camera

    if len(faceCascade.detectMultiScale(frame))>0:    # check the length of frame in detection               
        faces = faceCascade.detectMultiScale(frame)   # Detects faces of different sizes in the input image

        for (x, y, w, h) in faces:                    # To draw a rectangle in a face(x and y coordinate, width and height) 
            if w > 0:                                 # if width is greater than 0                            
                if len(eye_cascade.detectMultiScale(frame))>0:        # if lenth of eye frame is greater than 0
                    eyes = eye_cascade.detectMultiScale(frame)        # Detects eyes of different sizes in the input image 
                    for (ex, ey, ew, eh) in eyes:                     # To draw a rectangle in eyes
                        if ew > 0:                                    # if the eye width is greater then 0
                            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)        # making rectangle around eye  
                                           
                else:                                             
                    
                    cv2.putText(frame,'Driver is Drowsy or sleepy',(50, 50),font, 1,(255,0,0), 2, cv2.LINE_4)   # put text on frame      
                    winsound.Beep(frequency, duration)    # play beep sound 
    else:
        #print("1")
        cv2.putText(frame, 'Driver is not looking Straight', (50, 50),font, 1,(255,0,0), 2, cv2.LINE_4) 
                    
    key = cv2.waitKey(1)                                   
    if key == 27:        #quit frame on esc
        break

video.release()                                                        #release the frame
cv2.destroyWindow(title)                                               # De-allocate any associated memory usage 
