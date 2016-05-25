import cv2
import numpy as np

def encContour(i):
	'''
	To returns the contour which encloses the whold body of the person in the
	image

	Inputs:
		i : name of the file

	Outputs:
		the contour which encloses the whole body
	'''
	image=cv2.imread(i)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,8)
	x=np.zeros(image.shape,dtype=np.uint8)
	can=cv2.Canny(gray,120,200)
	closing=cv2.morphologyEx(can,cv2.MORPH_CLOSE,np.ones((8,8),np.uint8),iterations=2)
	contours,hei=cv2.findContours(closing.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) == 1 :
		return contours[0]
	else:
		k=0
		t=contours[0]
		for i in contours :
			if cv2.arcLength(t,True) < cv2.arcLength(i,True):
				t=i
		return t
