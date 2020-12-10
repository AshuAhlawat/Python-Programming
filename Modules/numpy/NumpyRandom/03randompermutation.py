from numpy import random
import numpy as np

#Shuffling arrays
arr=np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)


arr1=np.array([1,2,3,4,5])
print(random.permutation(arr1))
#Both shuffle and permutaion does the same job
