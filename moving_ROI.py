# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:51:59 2020

@author: vijay chauhan

copying ROI in some other part of the image
"""

import numpy as np
import cv2 as cv

img=cv.imread('1.jpg')

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',600,600)

car=img[2829:4544,480:2345]
img[2000:3715,2500:4365]=car

def x_(event,x,y,flag,param):
    if(event==cv.EVENT_LBUTTONDOWN):
        print(x,y)
cv.setMouseCallback('frame',x_)
cv.imshow('frame',img)



k=cv.waitKey(0)
if(k==27):
    cv.destroyAllWindows()