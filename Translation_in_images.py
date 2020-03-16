# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:58:34 2020

@author: vijay chauhan

Translation in images - moving left right
"""

import numpy as np
import cv2 as cv

img=cv.imread('blurred.jpg')

img=cv.resize(img,(400,400),interpolation=cv.INTER_AREA)
rows,cols=img.shape[:2]
m=np.float32([[1,0,-200],[0,1,120]])
print(m)
img=cv.warpAffine(img,m,(400,400))

img=img[120:,:200,:]
cv.namedWindow('frame',cv.WINDOW_NORMAL)
def call(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)

cv.setMouseCallback('frame',call)
img=cv.copyMakeBorder(img,220,200,200,200,cv.BORDER_REFLECT)
cv.imshow('frame',img)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()