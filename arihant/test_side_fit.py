import cv2
from cvt_small import cvt_small
from side_fit import side_fit


#head, body_without_head, head_side_view, side_view_without_head, hands, body_without_hands = \
#    parts_divide('reference_front_stretched.jpg', 'reference_side.jpg')
image = cv2.imread('test_side_without_head.jpg')

side_view_without_head = cv2.imread('reference_side_without_head.jpg')

image = cvt_small(image,800)
side_view_without_head = cvt_small(side_view_without_head,800)

reference = side_view_without_head.copy()

test, final_image = side_fit(image, reference)
cv2.imshow('test image', test)
cv2.imshow('final image after side modification', final_image)
cv2.waitKey(0)
