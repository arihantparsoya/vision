import cv2
import numpy as np
from outer import encContour
from parts import retval
from matplotlib import pyplot as plt
import copy

def parts_divide_hum(inpf,inps):
	imgf= inpf.copy()
	imgs= inps.copy()
	cont_f=encContour(imgf)
	cont_s=encContour(inps)


	#getting extreme points

	l=tuple(cont_f[cont_f[:,:,0].argmin()][0])
	r=tuple(cont_f[cont_f[:,:,0].argmax()][0])
	t=tuple(cont_f[cont_f[:,:,1].argmin()][0])
	b=tuple(cont_f[cont_f[:,:,1].argmax()][0])
	ls=tuple(cont_s[cont_s[:,:,0].argmin()][0])
	rs=tuple(cont_s[cont_s[:,:,0].argmax()][0])
	ts=tuple(cont_s[cont_s[:,:,1].argmin()][0])
	bs=tuple(cont_s[cont_s[:,:,1].argmax()][0])
	hi=b[1]-t[1]
	p=t[1]+0.4*hi
	x=retval(p,cont_f,0)
	ran=np.linspace(t[1],p,200)
	for i in range(0,200):
		ran[i]=p-ran[i]
		ran[i]=ran[i]+t[1]

	Y=[]
	a=0
	b=0
	#sorted(ran,reverse=True)
	for i in range(1,200):
		#i=-i
		#i=p+i
		yp=retval(ran[i-1],cont_f,0)
		y=retval(ran[i],cont_f,0)
		if len(yp)==2 and a==0:
			p_slope=yp[0]-y[0]
			a=1									#comparing slopes
			continue
		elif len(yp)==2 and len(y)==2 and a==1:
			#print len(yp)
			slope=yp[0]-y[0]
			print p_slope
			if p_slope!=0:
				b=1
				ratio=float(slope)/p_slope
				#print ratio
			p_slope=slope

		else:
			continue
		if b==1 and ratio>1.2:
			Y.append(y[0])
			Y.append(y[1])
			break
	imgf2 = inpf.copy()
	#imgf2=cv2.imread(inpf)
	height,width,dim=imgf2.shape
	img3=np.zeros((height,width,dim), dtype=np.uint8)
	img3[:,:]=[255,255,255]
	img4=np.zeros((height,width,dim), dtype=np.uint8)
	img4[:,:]=[255,255,255]
	img4[:,0:int(Y[0])]=imgf2[:,0:int(Y[0])]
	img4[:,int(Y[1]):int(width)]=imgf2[:,int(Y[1]):int(width)]			#projecting hands in blank image
	imgf2[:,0:int(Y[0])]=img3[:,0:int(Y[0])]											#removing hands from copy of original image
	imgf2[:,int(Y[1]):int(width)]=img3[:,int(Y[1]):int(width)]			#also taking the mirror image of one hand
	cv2.imwrite('handsi.jpg', img4)
	#plt.imshow(img4)
	#plt.show()
	cv2.imwrite('body_without_handsi.jpg', imgf2)
	#plt.imshow(imgf2)
	#plt.show()

	#for cutting head
	wid2=(r[0]-l[0])/4
	
	ran2=np.linspace(l[0]+wid2,r[0],300)
	q=0
	Z=[]
	for i in range(0,300):
		if i==0:
			continue
		z=retval(ran2[i],cont_f,1)
		zp=retval(ran2[i-1],cont_f,1)
		if a==0:
			p_slope=float(zp[0]-z[0])/(ran2[i]-ran2[i-1])
			a=1
		elif a==1:
			slope=float(zp[0]-z[0])/(ran2[i]-ran2[i-1])
			if p_slope!=0:
				ratio=float(slope)/p_slope
				#print ratio
			p_slope=slope
		if ratio>1.5:
			Z.append(zp[0])
			w=ran2[i]
			break
	#print len(Z)
	#imgf2=cv2.imread(inpf)
	imgf2 = inpf.copy()
	img1=np.zeros((height,width,dim), dtype=np.uint8)
	img1[:,:]=[255,255,255]
	img2=np.zeros((height,width,dim), dtype=np.uint8)
	img2[:,:]=[255,255,255]
	img2[0:int(Z[0]),:]=imgf[0:int(Z[0]),:]
	imgf[0:int(Z[0]),:]=img1[0:int(Z[0]),:]
	cv2.imwrite('headi.jpg', img2)
	#plt.imshow(img4)
	#plt.show()
	cv2.imwrite('body_without_headi.jpg', imgf)
	#plt.imshow(imgf2)
	#plt.show()

	#head side view

	cont_h=encContour(img2)
	th=tuple(cont_h[cont_h[:,:,1].argmin()][0])
	bh=tuple(cont_h[cont_h[:,:,1].argmax()][0])
	head_len=bh[1]-th[1]
	m=ts[1]+head_len
	imgs2=imgs.copy()
	hs,ws,ds=imgs2.shape
	img5=np.zeros((hs,ws,ds), dtype=np.uint8)
	img5[:,:]=[255,255,255]
	img6=np.zeros((hs,ws,ds), dtype=np.uint8)
	img6[:,:]=[255,255,255]
	img6[0:int(m),:]=imgs2[0:int(m),:]
	imgs2[0:int(m),:]=img5[0:int(m),:]
	cv2.imwrite('head_sidei.jpg', img6)
	#plt.imshow(img4)
	#plt.show()
	cv2.imwrite('body_without_head_sidei.jpg', imgs2)
	#plt.imshow(imgf2)
	#plt.show()

	return 'headi.jpg','body_without_headi.jpg','head_sidei.jpg','body_without_head_sidei.jpg', 'handsi.jpg','body_without_handsi.jpg',
