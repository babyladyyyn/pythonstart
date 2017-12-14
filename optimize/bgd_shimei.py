#!/usr/bin/env python
#by shimei

import numpy as np
import time

def bgd(sample,y,step_size=0.0001,max_loop_count=100000,max_error=0.00001):
	loop_index=1
	sample_count,feature_count=sample.shape
	feature_vector=np.zeros(feature_count)
	while True:
		if loop_index>=max_loop_count:
			break
		loop_index+=1
		offset_feature_vector=(step_size/sample_count)*(np.sum((y-np.dot(sample,feature_vector))*np.transpose(sample),axis=1))
		#print "offset_feature_vector",offset_feature_vector
		feature_vector=feature_vector+offset_feature_vector
		#print "feature_vector",feature_vector
		print "loop_index:",loop_index,"error:",(1.0/sample_count)*np.sum((y-np.dot(sample,feature_vector))**2)
		if (1.0/sample_count)*np.sum((y-np.dot(sample,feature_vector))**2)<=max_error:
			break
	return feature_vector



def main():
	sample_count=100000
	feature_count=30
	max_loop_count=10000
	max_error=0.00000000#1

	sample=np.random.rand(sample_count,feature_count)+0.5
	feature=np.random.rand(feature_count)*1+0.5
	y=np.dot(sample,feature)

	predict_feature=bgd(sample,y,step_size=0.01,max_loop_count=max_loop_count,max_error=max_error)

	#print "sample:",sample
	#print "y:",y
	print "feature:",feature
	print "predict_feature",predict_feature


if __name__ == "__main__":
	main()



