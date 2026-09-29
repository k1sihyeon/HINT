import numpy as np
import cv2 as cv

imgfile = 'C:\\dev\\opencv\\sources\\samples\\data\\lena.jpg'
img = cv.imread(imgfile, cv.IMREAD_COLOR)

cv.imshow('image', img)
cv.waitKey(0)