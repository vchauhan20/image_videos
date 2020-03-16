# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:33:42 2020

@author: Karan

adaptive thresholding with otsu' binarization
"""

import numpy as np
import cv2 as cv

img=cv.imread('1.jpg',0)

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',600,600)
cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1',600,600)
#img1=cv.GaussianBlur(img,(151,151),0)
ret,img2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('frame',img2)
img3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,501,2)
cv.imshow('frame1',img3)
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()