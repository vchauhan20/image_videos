# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:03:10 2020

@author: Karan

program to create a logo on an image
"""

import cv2 as cv

img=cv.imread('1.jpg')

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',600,600)

img=cv.putText(img,'Vijay',(40,1500),cv.FONT_HERSHEY_COMPLEX,80,(100,220,40),50)
img=cv.rectangle(img,(200,1600),(600,2600),(100,10,200),200)
cv.imshow('frame',img)

k=cv.waitKey(0)& 0xFF

if(k==27):
    cv.destroyAllWindows()