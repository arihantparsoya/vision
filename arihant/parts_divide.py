import cv2
import numpy as np
from outer import encContour
from matplotlib import pyplot as plt
import copy

def retval (t,f,co) :

		x=[]

		for i in range(0,len(f)-1):
			a=f[:,0,1-co][i]-t
			b=f[:,0,1-co][i+1]-t
			if a*b == 0 :
				if a==0:
					x.append(f[:,0,co][i])
				else:
					x.append(f[:,0,co][i+1])
			else:
				if a*b<0:
					x.append((f[:,0,co][i]+f[:,0,co][i+1])/2)
		sorted(x)

		y=[]
		for i in range(0,len(x)-1):
			if x[i] == x[i+1] :
				continue
			y.append(x[i])
		if len(x) is not 0 :
			y.append(x[-1])
		return y

def parts_divide(inpf, inps):
	'''
	inputs:
		inpf: input front image file
		inps: input side image file
	output:
		files for of:
			1. head
			2. body without head
			3. side view of head
			4. body without head side view
			5. hands(front view)
			6. body without hands(front view)
	'''
	imgf=cv2.imread(inpf)
	imgs=cv2.imread(inps)
	cont_f=encContour(imgf)
	cont_s=encContour(imgs)


#getting extreme points

	l=tuple(cont_f[cont_f[:,:,0].argmin()][0])
	r=tuple(cont_f[cont_f[:,:,0].argmax()][0])
	t=tuple(cont_f[cont_f[:,:,1].argmin()][0])
	b=tuple(cont_f[cont_f[:,:,1].argmax()][0])
	ls=tuple(cont_s[cont_s[:,:,0].argmin()][0])
	rs=tuple(cont_s[cont_s[:,:,0].argmax()][0])
	ts=tuple(cont_s[cont_s[:,:,1].argmin()][0])
	bs=tuple(cont_s[cont_s[:,:,1].argmax()][0])
	length=r[0]-l[0]
	ran=np.linspace(0,b[1],200)
	for i in range(0,200):
		if i==0:
			continue
		ran[i]=b[1]-ran[i]

	c=0
	z=0
	X=[]
	for i in ran:
		x11=retval(i,cont_f,0)     #0 for y-coordinate
		if z==1:
			break
		if len(x11)==2 and c==0:
			wl=x11[1]-x11[0]
			c=1
		if len(x11)==2 and c==1:
			nl=x11[1]-x11[0]
			if nl<0.65*wl:
				X.append([x11[0],b[1]-i])
				X.append([x11[1],b[1]-i])
				z=1
				break
	imgf1=imgf
	imgs1=imgs
	h,w,d=imgf.shape
	h2,w2,d2=imgs.shape
	img1=np.zeros((h,w,d), dtype=np.uint8)
	img1[:,:]=[255,255,255]
	img2=np.zeros((h,w,d), dtype=np.uint8)
	img2[:,:]=[255,255,255]
	img2[0:int(i),:]=imgf1[0:int(i),:]			#projecting the head in blank image
	imgf1[0:int(i),:]=img1[0:int(i),:]			#removing the head from copy of image
	head = img2.copy()
	#cv2.imwrite('head.jpg', img2)
	body_without_head = imgf1.copy()
	#cv2.imwrite('body_without_head.jpg', imgf1)
	dist=int(i-t[1])
	img5=np.zeros((h2,w2,d2), dtype=np.uint8)
	img5[:,:]=[255,255,255]
	img6=np.zeros((h2,w2,d2), dtype=np.uint8)
	img6[:,:]=[255,255,255]
	img6[0:ts[1]+dist,:]=imgs1[0:ts[1]+dist,:]			#projecting the head in blank image
	imgs1[0:ts[1]+dist,:]=img5[0:ts[1]+dist,:]
	head_side_view = img6.copy()
	#cv2.imwrite('head_side_view.jpg', img6)
	side_view_without_head = imgs1.copy()
	#cv2.imwrite('side_view_without_head.jpg', imgs1)

	#cv2.imshow(img2, 'head')
	Y=[]
	height,width,dim=imgf.shape
#for hands
	a=0
	b=0
	ran2=np.linspace(l[0]+(r[0]-l[0])/3,l[0]+(r[0]-l[0])/2,200)
	for i in range(1,200):
		yp=retval(ran2[i-1],cont_f,1)
		y=retval(ran2[i],cont_f,1)
		if len(y)!=2:
			continue
		if len(yp)==2 and a==0:
			p_slope=y[0]-yp[0]
			a=1									#comparing slopes
			continue
		elif len(yp)==2 and len(y)==2 and a==1:
			#print len(yp)
			slope=y[1]-yp[1]
			if p_slope!=0:
				b=1
				ratio=float(slope)/p_slope
				#print 'ratio', ratio,'coordinates',ran2[i]
			p_slope=slope

		else:
			continue
		if b==1 and ratio>1.5:
			j=ran2[i]
			#Y.append([i,y[1]])
			#Y.append([width-i,y[1]])
			#Y.append([i,y[0]])
			#Y.append([width-i,y[0]])
			break
	#print Y
	#print j
	imgf2=cv2.imread(inpf)
	img3=np.zeros((height,width,dim), dtype=np.uint8)
	img3[:,:]=[255,255,255]
	img4=np.zeros((height,width,dim), dtype=np.uint8)
	img4[:,:]=[255,255,255]
	img4[:,0:int(j)]=imgf2[:,0:int(j)]
	img4[:,int(width-j):int(width)]=imgf2[:,int(width-j):int(width)]			#projecting hands in blank image
	imgf2[:,0:int(j)]=img3[:,0:int(j)]											#removing hands from copy of original image
	imgf2[:,int(width-j):int(width)]=img3[:,int(width-j):int(width)]			#also taking the mirror image of one hand
	hands = img4.copy()
	body_without_hands = imgf2.copy()

	#cv2.imwrite('hands.jpg', img4)
	#cv2.imwrite('body_without_hands.jpg', imgf2)
	#img4=cv2.imread('hands.jpg')
	#imgf2=cv2.imread('body_without_hands.jpg')
	#plt.imshow(img4)
	#plt.show()
	#plt.imshow(imgf2)
	#plt.show()
	return head, body_without_head, head_side_view, side_view_without_head, hands, body_without_hands
