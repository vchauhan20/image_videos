# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:16:36 2020

@author: vijay chauhan

Merging two images one over the other
"""

import numpy as np
import cv2 as cv

start=cv.getTickCount()
img=cv.imread('1.jpg')
img1=cv.imread('4.jpg')
rows,cols,cul=img1.shape
roi=img[:rows,:cols,:cul]


cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)

cv.namedWindow('frame1',cv.WINDOW_NORMAL)
cv.resizeWindow('frame1',500,500)

cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame2',500,500)

logo_gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

ret,mask=cv.threshold(logo_gray,10,255,cv.THRESH_BINARY)

mask_inv=cv.bitwise_not(mask)

img_bg=cv.bitwise_and(roi,roi,mask=mask_inv)

img_fg=cv.bitwise_and(img1,img1,mask=mask)

final=cv.add(img_bg,img_fg)
img[:rows,:cols,:cul]=final

cv.imshow('frame',img)
cv.imshow('frame1',img1)
cv.imshow('frame2',img_fg)
end=cv.getTickCount()
print((end-start)/cv.getTickFrequency()) 


k=cv.waitKey(0)
if(k==27):
    cv.destroyAllWindows()

   