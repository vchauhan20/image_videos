# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:39:14 2020

@author: vijay chauhan

opencv programs : program to read and image using opencv
"""
import cv2 as cv

# reading the image in grayscale
img=cv.imread('1.jpg',0)
#displaying the image in window named frame

cv.imshow('frame',img)

# waiting indefinetly for any key to be pressed
k=cv.waitKey(0)& 0xFF

# if 's' is pressed imaged in saved in local folder and 
#all windows are destroyed
if(k==ord('s')):
    img=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    cv.imshow('frame2',img)
    
    cv.imwrite('mountains.jpg',img)
    cv.destroyAllWindows()
# else all windows are destroyed
else:    
    
    cv.destroyAllWindows()
    