from outer import encContour
from height import height
from plot import plot_contour
from matplotlib import pyplot as plt
import cv2
import numpy as np
import copy
import math
import sys

url = '4.jpg'
cnt = encContour(url)
plot_contour(cnt1= cnt, cnt2= cnt, axis1='X')
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
