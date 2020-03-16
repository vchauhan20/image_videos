# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:22:37 2020

@author: vijay chauhan 

Face detection in an music video
"""

import numpy as np
import cv2 as cv
face=cv.CascadeClassifier('face.xml')


cap=cv.VideoCapture('11.mp4')
while(cap.isOpened()):
    ret,frame=cap.read()
    frame1=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(frame1,scaleFactor=1.5,minNeighbors=5)
    for x,y,h,w in faces:
        cv.rectangle(frame,(x,y),(x+h,y+w),(0,0,255))
    cv.imshow('frame',frame)
    k=cv.waitKey(20)
    if k==27:
        break
cap.release()
cv.destroyAllWindows()    
    