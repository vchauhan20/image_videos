# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:39:22 2020

@author: vijay chauhan

Padding around the images
"""

import numpy as np
import cv2 as cv

img=cv.imread('1.jpg')

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame' ,500,500)
cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1' ,500,500)
cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame2' ,500,500)
cv.namedWindow('frame3',cv.WINDOW_NORMAL)
cv.resizeWindow('frame3' ,500,500)
cv.namedWindow('frame4',cv.WINDOW_NORMAL)
cv.resizeWindow('frame4' ,500,500)

img1=cv.copyMakeBorder(img,350,250,1550,450,cv.BORDER_REPLICATE)
img2=cv.copyMakeBorder(img,350,250,1550,450,cv.BORDER_REFLECT)
img3=cv.copyMakeBorder(img,350,250,1550,450,cv.BORDER_WRAP)
img4=cv.copyMakeBorder(img,350,250,1550,450,cv.BORDER_CONSTANT,(30,190,40))
cv.imshow('frame',img1)
cv.imshow('frame1',img)
cv.imshow('frame2',img2)
cv.imshow('frame3',img3)
cv.imshow('frame4',img4)
k=cv.waitKey(0)

if(k==27):
    cv.destroyAllWindows()