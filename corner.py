import cv2
import numpy as np

def corner_det(img):
	im=cv2.imread(img)
	gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	gray=np.float32(gray)
	cor=cv2.cornerHarris(gray,5,3,0.04)
	im[cor>0.01*cor.max()]=[0,0,255]
	cv2.imshow('dst', im)
	cv2.waitKey(0)
	
	
