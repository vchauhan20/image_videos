# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:52:21 2020

@author: vijay chauhan
Perpective Transformations

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('1_copy.jpg')
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',300,300)
rows,cols=img.shape[:2]
def call(event,x,y,flag,param):
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,y)
cv.setMouseCallback('frame',call)        

pt1 = np.float32([[43,166],[172,172],[21,283],[165,281]])
pt2 = np.float32([[0,0],[600,0],[0,300],[300,300]])
m=cv.getPerspectiveTransform(pt1,pt2)

img=cv.warpPerspective(img,m,(300,300))
cv.imshow('frame',img)
cv.waitKey(10000)
cv.destroyAllWindows()