# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:49:50 2020

@author: vijay chuahan

Paint application with varying brush size
"""

import numpy as np
import cv2 as cv
rad=0
s=0
r,g,b=200,0,0
img=cv.imread('1.jpg')
img1=img.copy()
print(img1)
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',800,800)

def brush_radius(x):
    rad=s
def reset(x):
    img=img1
    
cv.createTrackbar('red','frame',0,255,brush_radius)
cv.createTrackbar('blue','frame',0,255,brush_radius)
cv.createTrackbar('green','frame',0,255,brush_radius)
cv.createTrackbar('brush','frame',0,200,brush_radius)
cv.createTrackbar('reset','frame',0,1,reset)
def calls(event,x,y,flag,param):
    if(event==cv.EVENT_MOUSEMOVE):
        print(x,y,rad,r,g,b)
        cv.circle(img,(x,y),rad,(b,g,r),20)
cv.setMouseCallback('frame',calls)        
while(1):
    
    cv.imshow('frame',img)
    r=cv.getTrackbarPos('red','frame')
    g=cv.getTrackbarPos('green','frame')
    b=cv.getTrackbarPos('blue','frame')
    s=cv.getTrackbarPos('brush','frame')
    res=cv.getTrackbarPos('reset','frame')
    rad=s
    if res==1:
        img=img1.copy()
    #img[:]=[r,g,b]
    k=cv.waitKey(1) & 0xFF
    
    if(k==27):
        break
cv.destroyAllWindows()
    