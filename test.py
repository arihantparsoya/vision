from outer import encContour
from height import height
from matplotlib import pyplot as plt
import cv2
import numpy as np
import copy
import math
import sys


image = cv2.imread('1.jpg')
cnt = encContour('1.jpg')
cv2.drawContours(image,cnt,-1,(255),3)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
