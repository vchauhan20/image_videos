# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 22:33:08 2020

@author: Karan

"""


import numpy as np
import cv2 as cv


img=cv.imread('1.jpg')
img1=cv.imread('4.jpg')
rows,cols,cul=img1.shape

img[0:rows,0:cols,:cul]=img1
cv.namedWindow('frame2',cv.WINDOW_NORMAL)
cv.resizeWindow('frame2',500,500)


cv.imshow('frame2',img)


print(cv.useOptimized())

k=cv.waitKey(0)
if(k==27):
    cv.destroyAllWindows()