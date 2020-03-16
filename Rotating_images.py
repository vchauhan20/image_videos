# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:29:57 2020

@author: Karan
"""

import numpy as np
import cv2 as cv

img=cv.imread('1.jpg')
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',600,600)
cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1',600,600)
rows,cols=img.shape[:2]
print(img.shape)
m=cv.getRotationMatrix2D((cols/2,rows/2),180,1)
img1=cv.warpAffine(img,m,(cols,rows))
cv.imshow('frame',img)
cv.imshow('frame1',img1)
k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()