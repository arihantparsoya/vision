#!usr/bin/python
import sys
import cv2
import numpy as np
'''
import os
os.mkdir('new')
os.chdir('new')	
os.chdir('../')
#except :	
#	os.mkdir('new')

'''
def cvt_small(oi,height) :
	scale=float(height)/oi.shape[0]
	#oi=cv2.imread(i)
	ni=cv2.resize(oi,(int(oi.shape[1]*scale),height),interpolation=cv2.INTER_CUBIC)
	return ni

