import cv2
from outer import encContour
from cvt_small import cvt_small

'''
 This is the test file of ret_hscale
 assuming that the real image is girl_front.jpg (as the hands down image of man.jpg was not available :P ) and model image is mfront.jpg
'''

image = cv2.imread('test_side.jpg')
resized_image = cvt_small(image,800)
contour_of_resized_image = encContour(resized_image)
cv2.drawContours(resized_image, contour_of_resized_image, -1 ,(255),2)
cv2.imshow('final',resized_image)
cv2.waitKey(0)
