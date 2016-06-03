import cv2
import numpy as np
from outer import encContour

def find_height(img,prop):
	cont=encContour(img)
	t=tuple(cont[cont[:,:,1].argmin()][0])
	b=tuple(cont[cont[:,:,1].argmax()][0])
	h=t[0][1]-b[0][1]
	if h<0:
		h=-h
	return prop*h
