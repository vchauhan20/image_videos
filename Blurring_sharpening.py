# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:40:43 2020

@author: vijay chauhan

Blurring and sharpening an image
cv.blur(imgae,kernel size)
cv.medianBlur(image,kernelsize)
cv.gaussianBlur(image,kernelsize,0)
cv.bilateralFilter(image,diameter of space kernel, sigma for x ,sigma for y)

"""

import cv2 as cv
import numpy as np

img=cv.imread('1.jpg')
kernel=np.ones((5,5),np.float32)/25

img1=cv.filter2D(img,-1,kernel)
cv.imshow('frame',img1)
img2=cv.blur(img,(5,5))
cv.imshow('frame2',img2)
img4=cv.GaussianBlur(img,(5,5),0)
cv.imshow('gaussian',img4)
img3=cv.bilateralFilter(img,125,10,10)
cv.imshow('frame3',img3)

cv.waitKey(10000)
cv.destroyAllWindows()