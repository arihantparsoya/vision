import cv2
import numpy as np
from outer import encContour

def find_distance(img, width):
	cont=encContour(img)
	l=tuple(cont[cont[:,:,0].argmin()][0])
	r=tuple(cont[cont[:,:,0].argmax()][0])
	wid_px=r[0][0]-l[0][0]
	#distance=original width*focal length/width in pixels
	return width*f/wid_px
	
