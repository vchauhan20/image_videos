# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:39:14 2020

@author: vijay chauhan

opencv programs : program to read and video from a file using opencv
"""
import cv2 as cv

#creating a video capture object
cap=cv.VideoCapture(0)
four_cc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('vijay.mp4',four_cc,20.0,(640,480))
# reading while the connection is opened
while(cap.isOpened()):
    
    # reading the image
    tag,img=cap.read()
    # tag returns true display the image in the frame
    if(tag):
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',img)
        out.write(img)
        k=cv.waitKey(30)&0xFF
        # if esc is pressed cap is released and all windows are destroyed
        if(k==27):
            out.release()
            cap.release()
            cv.destroyAllWindows()
    else:
        break
cap.release()    
out.release()
cv.destroyAllWindows()    
        
    