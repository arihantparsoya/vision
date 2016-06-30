from resize_model import resize_model
import cv2
from cvt_small import cvt_small
from matplotlib import pyplot as plt

rimg = cv2.imread('x1.jpg')
mfrontf = cv2.imread('man_frontf.jpg')
mfront = cv2.imread('man_front.jpg')
mside = cv2.imread('man_side.jpg')
rimg = cvt_small(rimg,800)

resized_mfront , resized_mfrontf , resized_mside = \
	resize_model(mfront , mfrontf , mside , rimg)

plt.subplot(231),plt.imshow(resized_mfront,'gray'),plt.title('resized_mfront')
plt.subplot(232),plt.imshow(resized_mfrontf,'gray'),plt.title('resized_mfrontf')
plt.subplot(233),plt.imshow(resized_mside,'gray'),plt.title('resized_mside')
plt.subplot(234),plt.imshow(rimg,'gray'),plt.title('rimg')

plt.show()
