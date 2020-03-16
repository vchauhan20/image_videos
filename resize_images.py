# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:36:33 2020

@author: vijay chauhan

resize and image in different ways
"""

import cv2 as cv
import numpy as np

img=cv.imread('blurred.jpg')
img=cv.resize(img,(600,400),interpolation=cv.INTER_AREA)

cv.imshow('frame',img)

k=cv.waitKey(0)
if k==27:
    cv.destroyAllWindows()