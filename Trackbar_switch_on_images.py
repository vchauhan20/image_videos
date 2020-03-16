# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:11:45 2020

@author: creatong trackbars and switch on the images
"""

import cv2 as cv
import numpy as np
img=np.zeros((400,400,3),np.uint8)
cv.namedWindow('frame',cv.WINDOW_NORMAL)
def calls(x):
    cv.putText(img,'here',(10,300),cv.FONT_HERSHEY_COMPLEX,5,(200,100,100),10)

cv.createTrackbar('Red','frame',0,255,calls)
cv.createTrackbar('blue','frame',0,255,calls)
cv.createTrackbar('green','frame',0,255,calls)
switch='OFF:0 \n ON:1'
cv.createTrackbar(switch,'frame',0,1,calls)

while(1):
    
    r=cv.getTrackbarPos('Red','frame')
    b=cv.getTrackbarPos('blue','frame')
    g=cv.getTrackbarPos('green','frame')
    s=cv.getTrackbarPos(switch,'frame')
    
    
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
        cv.circle(img,(200,200),30,(r,g,b),-1)
        print(img)
    
    cv.imshow('frame',img)
    k=cv.waitKey(1)& 0xFF
    if k==27:
        break
    
    
    
    
    
cv.destroyAllWindows()