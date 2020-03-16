# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:59:59 2020

@author: vijay chauhan

Affine transformations
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('1.jpg')
cv.namedWindow('frame',cv.WINDOW_NORMAL)
cv.resizeWindow('frame',500,500)
rows,cols=img.shape[:2]
        
pt1 = np.float32([[50,50],[200,50],[50,200]])
pt2 = np.float32([[10,100],[200,50],[100,250]])
m=cv.getAffineTransform(pt1,pt2)

img=cv.warpAffine(img,m,(cols,rows))

cv.imshow('frame',img)
cv.waitKey(10000)
cv.destroyAllWindows()

