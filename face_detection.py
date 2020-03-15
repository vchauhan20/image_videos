# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:57:52 2020

@author: vijay chauhan

Face detection
"""

import cv2 as cv
face_cascade=cv.CascadeClassifier('vj.xml' )
face1_cascade=cv.CascadeClassifier('haarcascade_smile.xml' )
full_body=cv.CascadeClassifier('haarcascade_fullbody.xml')
smile=cv.CascadeClassifier('smile.xml')
cap=cv.VideoCapture(0);

while(cap.isOpened()):
    ret,frame=cap.read()
    #frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.namedWindow('frame1',cv.WINDOW_NORMAL)
    cv.resizeWindow('frame1',900,800)   
    faces=face_cascade.detectMultiScale(frame,1.2,4)
    smile=face1_cascade.detectMultiScale(frame,1.2,4)
    ful=full_body.detectMultiScale(frame,1.2,4)
    #for(x,y,w,h) in ful:
       # cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    for (x,y,w,h)in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    """for (x,y,w,h)in smile:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    """
    cv.imshow('frame1',frame) 
    if(cv.waitKey(1)==27):
        break
cap.release()
cv.destroyAllWindows()   