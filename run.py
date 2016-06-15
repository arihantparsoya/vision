import cv2
import numpy as np
from man_hands import cor_hands
from outer import encContour
img=cor_hands('mfront.jpg','mside.jpg','mfront.jpg','mside.jpg')
cv2.imwrite('TEST_new.jpg',img)
