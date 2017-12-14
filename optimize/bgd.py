#!/usr/bin/env python

import numpy as np
import time

step_size=0.01
max_loop_count=10000
default_sitan=np.zeros(n)
xn=np.random.rand(1000,n)*10+0.5
pn=np.random.rand(n)*1+0.5
yn=np.dot(xn,pn)



def bgd(samples,y,step_size=step_size,max_iter_count=max_iter_count):
	samples_count,dim=samples.shape
	index=0
	rpn=np.zeros((dim,),dtype=np.float32)
	while True:
		index+=1
		if index>max_iter_count:
			break

	pass
	
