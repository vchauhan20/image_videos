# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:46:07 2020

@author: Karan

Drawing different shapes on images depending on what is pressed
"""

import cv2 as cv
img=cv.imread('1.jpg')
mode=False
drawing=True
ix=-1
iy=-1
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)

def calls(event,x,y,flag,param):
    global ix,iy,mode,drawing
    ix=x
    iy=y
    if(event==cv.EVENT_LBUTTONDOWN):
        print('i m here')
        drawing=not drawing
        if mode==True:
            cv.rectangle(img,(x,y),(x+300,y+400),(108,100,130),-1)
        else:
            cv.circle(img,(x,y),250,(200,90,100),-1)
            
    
    if event==cv.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv.rectangle(img,(x,y),(x+300,y+400),(108,100,130),-1)
            else:
                cv.circle(img,(x,y),250,(200,90,100),-1)
                
        
        
        
        
        
cv.setMouseCallback('frame',calls)
while(1):
    cv.imshow('frame',img)
    k=cv.waitKey(100)& 0xFF
    if(k==ord('m')):
        mode=not mode
    if k==27:
        break
cv.destroyAllWindows()
    