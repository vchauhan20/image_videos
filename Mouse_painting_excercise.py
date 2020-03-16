# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 21:13:23 2020

@author: vijay chauhan

Mouse as a point brush
"""

import numpy as np

import cv2 as cv

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)
img2=np.ones((300,300,3),np.uint16)
cv.imshow('frame2',img2)
img=cv.imread('beach.jfif')

def nothing(x):
    x=2
cv.createTrackbar('red','frame',0,255,nothing)

while(1):
    cv.imshow('frame',img)
    r=cv.getTrackbarPos('red','frame')
    img[:,:,2]=r
    
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
cv.destroyAllWindows()