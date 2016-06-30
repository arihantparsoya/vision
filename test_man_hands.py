import cv2
import numpy as np
from man_hands import man_hands
from outer import encContour
img=man_hands('scaled_mfrontf11.jpg', 'mside.jpg','ar1.jpg', 'mside.jpg')
cv2.imwrite('TEST_new.jpg',img)
