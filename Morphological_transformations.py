# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:36:22 2020

@author: vijay chauhan

Morphological Transformations
"""

import cv2 as cv
import numpy as np

img=cv.imread('4.jpg',0)
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1',500,500)
cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)
cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame2',500,500)
kernel=np.ones((23,23),np.uint16)
img1=cv.erode(img,kernel,iterations=1)
img2=cv.dilate(img,kernel,iterations=1)
img3=cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
img4=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
img5=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
img6=cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)
cv.imshow('frame',img5)
cv.imshow('frame1',img6)
cv.imshow('frame2',img4)
cv.waitKey(10000)
cv.destroyWindow('frame')
cv.destroyWindow('frame1')
cv.destroyAllWindows()
