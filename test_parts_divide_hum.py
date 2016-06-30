from parts_divide_hum import parts_divide_hum
import cv2
from cvt_small import cvt_small
from resize_image import resize_image
x = cv2.imread('pri_f.jpg')
x1=cv2.imread('pri_s.jpg')
y=cvt_small(x,800)
y1=cvt_small(x1,800)
imgf,imgs=resize_image(y,y1)
parts_divide_hum = parts_divide_hum(y,y1)
