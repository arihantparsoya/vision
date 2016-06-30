import cv2
from plot3d import plot3dHuman2
from plot3d import plot3dHuman
from ret2Val import ret2Val
from resize_model import resize_model
from ret_hscale import ret_hscale
from outer import encContour
from cvt_small import cvt_small
'''
 This is the test file of ret_hscale
 assuming that the real image is girl_front.jpg (as the hands down image of man.jpg was not available :P ) and model image is mfront.jpg
'''
#resize_model('man_front.jpg','man_frontf.jpg','man_side.jpg','girl_front.jpg')
#a=ret2Val('mfront.jpg')
#ret_hscale('girl_front.jpg','mfront.jpg',('mfront.jpg','mfrontf.jpg'))
#plot3dHuman2('body_without_hands.jpg','hands.jpg','man_side.jpg',[])

#from outer import encContour
image = cv2.imread('x1.jpg')
resized_image = cvt_small(image,800)
contour_of_resized_image = encContour(resized_image)
cv2.drawContours(resized_image, contour_of_resized_image, -1 ,(255),2)
cv2.imshow('final',resized_image)
cv2.waitKey(0)
