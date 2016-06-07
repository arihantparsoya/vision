import cv2
import numpy as np
from outer import encContour

def join_points(inpf, inps):
	imgf=cv2.imread(inpf)
	imgs=cv2.imread(inps)
	cont_f=encContour(inpf)
	cont_s=encContour(inps)
#to traverse through x and y coordinates(Rahul's fn.)
	def retval (t,f,co) :
		x=[]
		for i in range(0,len(f)-1):
			a=f[:,1-co][i]-t
			b=f[:,1-co][i+1]-t
			if a*b == 0 :
				if a==0:
					x.append(f[:,co][i])
				else:
					x.append(f[:,co][i+1])
			else:
				if a*b<0:
					x.append((f[:,co][i]+f[:,co][i+1])/2)
		sorted(x)
		
		y=[]
		for i in range(0,len(x)-1):
			if x[i] == x[i+1] :
				continue
			y.append(x[i])
		if len(x) is not 0 :
			y.append(x[-1])
		return y

#getting extreme points

	l=tuple(cont_f[cont_f[:,:,0].argmin()][0])
	r=tuple(cont_f[cont_f[:,:,0].argmax()][0])
	t=tuple(cont_f[cont_f[:,:,1].argmin()][0])
	b=tuple(cont_f[cont_f[:,:,1].argmax()][0])
	length=r[0]-l[0]
	ran=np.linspace(0,b[1],200)
	for i in ran:
		if i==0:
			continue
		ran[i-1]=b[1]-ran[i-1]
		
	c=0
	z=0
	X=[]
	for i in ran:
		x=retval(i,cont_f,0)     #0 for y-coordinate
		if z==1:
			break
		if len(x)==2 and c==0:
			wl=x[1]-x[0]
			c=1
		elif len(x)==2 and c==1:
			nl=x[1]-x[0]
			if nl<0.75*wl:
				X.append(x[0],b[1]-i)
				X.append(x[1],b[1]-i)
				z=1
				break
	imgf1=imgf
	imgs1=imgs
	img1=np.zeros((512,512,3), dtype=np.uint8)
	img2=np.zeros((512,512,3), dtype=np.uint8)
	img2[0:b[1]-i,1]=imgf1[0:b[1]-i,1]			#projecting the head in blank image
	imgf1[0:b[1]-i,1]=img1[0:b[1]-i,1]			#removing the head from copy of image
	cv2.imwrite('head', img2)
	cv2.imwrite('hh', imgf1)
	#cv2.imshow(img2, 'head')
	Y=[]
	height,width,dim=imgf.shape
#for hands	
	for i in range(0.5,r[0],0.5):
		yp=retval(i-0.5,cont_f,1)
		y=retval(i,cont_f,1)
		if i==0.5:
			p_slope=(y[1]-yp[1])*2			#comparing slopes
			continue
		slope=(y[1]-yp[1])*2
		if p_slope!=0:
			ratio=slope/p_slope
		else: 
			continue
		p_slope=slope
		if ratio>1.5:
			Y.append(i,y[1])
			Y.append(width-i,y[1])
			Y.append(i,y[0])
			Y.append(width-i,y[0])
			break
		
	imgf2=imgf
	imgs2=imgs
	img3=np.zeros((512,512,3), dtype=np.uint8)
	img4=np.zeros((512,512,3), dtype=np.uint8)
	img4[0:i,0]=imgf2[0:i,0]
	img4[width-i:width,0]=imgf2[width-i:width,0]			#projecting hands in blank image
	imgf2[0:i,0]=img3[0:i,0]								#removing hands from copy of original image
	imgf2[width-i:width,0]=img3[width-i:width,0]			#also taking the mirror image of one hand
	cv2.imwrite('hands', img4)
	cv2.imwrite('fj', imgf2)
	
	return img2,imgf1,img4,imgf2
		
			
		
		
		
