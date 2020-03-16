# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:23:18 2020

@author: vijay chauhan

Edge Dection in images using thresholding
"""

import numpy as np
import cv2 as cv

img=cv.imread('1.jpg')
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',600,600)
cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame2',600,600)
cv.namedWindow('frame3',cv.WINDOW_NORMAL)
cv.resizeWindow('frame3',600,600)
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img2=cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,711,5)
img3=cv.adaptiveThreshold(img1,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,711,5)
cv.imshow('frame',img1)
cv.imshow('frame2',img2)
cv.imshow('frame3',img3)
k=cv.waitKey(0) & 0xFF

if(k==27):
    cv.destroyAllWindows()
    