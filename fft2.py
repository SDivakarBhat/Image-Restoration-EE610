import sys
import random
import numpy as np
from cmath import exp, pi
from fft import FFT

def fft2(image):
        x = np.zeros_like(image)
	y = np.zeros_like(image)
	x = np.array(image)
	
	(N1,N2) = image.shape[:2]
	#print(N1, N2)
#	print(image);
	t = 0
	b = 1024-N2
	l = 0
	r = 1024-N1


	np.pad(x, ((t,b),(l,r)), 'constant')
	
	#np.pad(x, ((1024-N1),(1024-N1)), 'constant', constant_values=(0, 0))
	
	print(x)
	for i in range(0,x.shape[0]):
		#print(x[i,:])		
		x[i,:] = np.trim_zeros(FFT(x[i,:]))
	
	y = np.transpose(x)

	#np.pad(y, ((1024-N2),(1024-N2)), 'constant', constant_values=(0, 0))

       	for i in range(0,y.shape[0]):
		x[:,i] = np.trim_zeros(FFT(y[:,i]))
	return x


