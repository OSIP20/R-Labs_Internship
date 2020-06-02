'''

startDate:  28 - 05 -2020
Project  :  Gesture Recognition
Part     :  Hand Detection with OpenCV
Libraries:  OpenCV (3.4.2),
            numpy (latest)
Team ID  :  4

'''

# importing required libraries..
import cv2
import numpy as np

# global Varibles
bckimg = None
kernalOpen = np.ones((2, 2))                                                     #MORPH takes numpy array
kernalClose = np.ones((1, 1))

#-----------------
# MAIN FUNCTION
#-----------------

if __name__ == "__main__":

    camera = cv2.VideoCapture(0)    
    (top, left), (bottom, right) = (250, 41), (419, 210)                         #co-ordinates of region of interest
    num_frames = 0

    while True:
        read, img = camera.read()
        img = cv2.resize(img, (420, 316))                                        # aspect ratio of 4:3
        img = cv2.flip(img, 1)
        
        cv2.rectangle(img, (top, left), (bottom, right), (0,255,0), 2)
                
        roi = img[left:right, top:bottom]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi = cv2.GaussianBlur(roi, (1, 1), 0)
        
        if num_frames < 5:                                                       #taking average of 5 frames
            if bckimg is None:                                                   #for first frame
                bckimg = roi
            else:
                cv2.accumulateWeighted(roi, bckimg.astype("float"), 0.4)         #weighted average of pics only takes float values
                   
        else:
            diff = cv2.absdiff(bckimg.astype("uint8"), roi)                      #takes difference with those averaged pics
            diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)[1]            #thresholding GRAY img
            diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernalOpen)            #MORPHING for ignoring small dots
            diff = cv2.morphologyEx(diff, cv2.MORPH_CLOSE, kernalClose)          #filling blank space in hand
            diff = cv2.resize(diff, (350, 350))
            cv2.imshow('difference', diff)
        
        
        cv2.imshow('ROI', roi)
        cv2.imshow('Original_Image', img)
        
        num_frames += 1
        
        keyPressed = cv2.waitKey(1) & 0xFF                                       #ESC key to terminate and 0xFF for 64-bit computers
        if keyPressed == 27:
            break
        
        
    camera.release()
    cv2.destroyAllWindows()    

