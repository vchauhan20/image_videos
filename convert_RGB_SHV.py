# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:24:04 2020

@author: vijay chauhan

finding the hsv value for any color
"""
import numpy as np
import cv2 as cv

red=np.uint8([[[0,0,255]]])

c=cv.cvtColor(red,cv.COLOR_BGR2HSV)
print(c)