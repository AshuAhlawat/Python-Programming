import numpy as np

# converting 1-D to 2-D
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)

# converting 1-D to 3-D
newarr=arr.reshape(2,3,2)
print(newarr)

# we cant reshape any  array the must be organized that every element must be filled no array will be blank like :
test_arr=np.array([1,2,3,4,5,6,7,8]) # number of element 8
#new_test_arr=test_arr.reshape(3,3) # total number required 9
#print(new_test_arr) #  output gives an error
print(test_arr.reshape(2,4).base)

arr2=np.array([1,2,3,4,5,6,7,8])
newarr1=arr2.reshape(2,2,-1)
print(newarr1)

#convert 2-D array to 1-D array
arr2d=np.array([[1,2,3,4],[5,6,7,8]])
arr2dr=arr2d.reshape(-1)
print(arr2dr)
