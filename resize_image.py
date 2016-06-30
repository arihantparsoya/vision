import cv2
import numpy as np
from outer import encContour
def resize_image(imgf,imgs):
	f=encContour(imgf)
	s=encContour(imgs)
	ft=tuple(f[f[:,:,1].argmin()][0])
	fb=tuple(f[f[:,:,1].argmax()][0])
	st=tuple(s[s[:,:,1].argmin()][0])
	sb=tuple(s[s[:,:,1].argmax()][0])
	
	fh=fb[1]-ft[1]
	sh=sb[1]-st[1]
	ratio=fh/sh
	s[:,0,1]=(s[:,0,1]-st[1])*ratio+st[1]
	cv2.drawContours(imgs,s,0,(255),2)
	return imgf,imgs
