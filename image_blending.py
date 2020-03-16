# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:45:58 2020

@author: vijay chauhan 

blending images 

"""
import numpy as np
import cv2 as cv

img1=cv.imread('1.jpg')
img2=cv.imread('4.jpg')

cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1',600,600)
cv.resizeWindow('frame2',500,500)

row,col,channels=img2.shape
roi=img1[:row,:col]
gray_img2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

ret,mask=cv.inRange(gray_img2,150,255)
mask_inv=cv.bitwise_not(mask)

img_bg=cv.bitwise_and(roi,roi,mask=mask_inv)
img_fg=cv.bitwise_and(img2,img2,mask=mask)

dst=cv.add(img_bg,img_fg)
img1[:row,:col]=dst
cv.imshow('frame1',mask)
cv.imshow('frame2',img1)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()