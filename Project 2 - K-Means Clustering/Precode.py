import numpy as np
import random

data = np.load('AllSamples.npy')

def initial_point_idx(id, k,N):
	return np.random.RandomState(seed=(id+k)).permutation(N)[:k]

def init_point(data, idx):
    return data[idx,:]

def initial_S1(id, k1):
    #print("Strategy 1: k and initial points")
    i = int(id)%150 
    random.seed(i+500)

    init_idx = initial_point_idx(i,k1,data.shape[0])
    init_s1 = init_point(data, init_idx)

    return k1, init_s1