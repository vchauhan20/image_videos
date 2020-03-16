# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:50:31 2020

@author: Karan

opencv programs : program to draw lines and shapes on an image
"""

import cv2 as cv

img=cv.imread('1.jpg')

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)

img=cv.line(img,(100,100),(1200,1500),(200,10,50),100,cv.LINE_AA)
img=cv.circle(img,(200,300),300,(100,220,10),200)
cv.imshow('frame',img)

k=cv.waitKey(0) & 0xFF
if(k==27):
    cv.destroyAllWindows()