#from matplotlib import pyplot as plt
from cvt_small import cvt_small
import cv2
x=cv2.imread('pri_f.jpg')
y=cvt_small(x,800)
print "Original image shape: ",x.shape,"\nResized image shape: ",y.shape
cv2.imshow('resized image',y)
cv2.waitKey(0)
#plt.imshow(y)
#plt.show()
