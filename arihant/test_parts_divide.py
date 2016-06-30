import cv2
import numpy as np
from matplotlib import pyplot as plt
from parts_divide import parts_divide

head, body_without_head, head_side_view, side_view_without_head, hands, body_without_hands = \
    parts_divide('reference_front_stretched.jpg', 'reference_side.jpg')

plt.subplot(231),plt.imshow(head,'gray'),plt.title('head')
plt.subplot(232),plt.imshow(body_without_head,'gray'),plt.title('body_without_head')
plt.subplot(233),plt.imshow(head_side_view,'gray'),plt.title('head_side_view')
plt.subplot(234),plt.imshow(side_view_without_head,'gray'),plt.title('side_view_without_head')
plt.subplot(235),plt.imshow(hands,'gray'),plt.title('hands')
plt.subplot(236),plt.imshow(body_without_hands,'gray'),plt.title('body_without_hands')

plt.show()
