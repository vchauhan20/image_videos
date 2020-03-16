# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:55:41 2020

@author: vijay chauhan

detecting  colored object in a video
"""
import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)
upper_red=np.array([10,255,255])
lower_red=np.array([0,255,255])
low_blue=np.array([110,50,50])
high_blue=np.array([130,255,255])
low_green=np.array([50,255,255])
high_green=np.array([70,255,255])  
while(cap.isOpened()):
    ret,frame=cap.read()
    
    if(ret):
        frame1=frame
        frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        
        mask_red=cv.inRange(frame,lower_red,upper_red)
        mask_blue=cv.inRange(frame,low_blue,high_blue)
        mask_green=cv.inRange(frame,low_green,high_green)
        fra_green=cv.bitwise_and(frame,frame,mask=mask_green)
        fra_red=cv.bitwise_and(frame,frame,mask=mask_red)
        fra_blue=cv.bitwise_and(frame,frame,mask=mask_blue)
        cv.imshow('red',fra_red)
        cv.imshow('blue',fra_blue)
        cv.imshow('original',frame1)
        cv.imshow('green',fra_green)
        
        k=cv.waitKey(30) & 0xFF
        if(k==27):
            break
    
    
    else:
        break
     
cap.release()
cv.destroyAllWindows()    