from outer import encContour
from height import height
from plot import plot_contour
from matplotlib import pyplot as plt
import cv2
import numpy as np
import copy
import math
import sys

cnt1 = encContour('man_front.jpg')
cnt2 = encContour('man_side.jpg')
image = cv2.imread('man_front.jpg')
plot_contour(cnt1= cnt1, cnt2= cnt2)
cv2.drawContours(image,cnt1,-1,(255),3)
cv2.imshow('front image',image)
cv2.waitKey(0)
#print((cnt))
'''
#test for encContour
image = cv2.imread(url)
cnt = encContour(url)
cv2.drawContours(image,cnt,-1,(255),3)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
