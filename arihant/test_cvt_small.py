from cvt_small import cvt_small
import cv2
x=cv2.imread('test_side.jpg')
y=cvt_small(x,800)
print "Original image shape: ",x.shape,"\nResized image shape: ",y.shape
cv2.imshow('resized image',y)
cv2.waitKey(0)
