# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 01:17:24 2020

@author: Karan

drawing circles on an image using mouse  double clicks
"""

import cv2 as cv

img=cv.imread('1.jpg')

cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',400,400)

def calls(event,x,y,flags,param):
    if(event==cv.EVENT_LBUTTONDBLCLK):
        #cv.line(img,(x,y),(600,600),(200,10,180),50)
        cv.circle(img,(x,y),100,(10,90,160),50)
cv.setMouseCallback('frame',calls)        
while(1):
    
    cv.imshow('frame',img)
    
    k=cv.waitKey(5)
    if(k==27):
        break
cv.destroyAllWindows()    
        