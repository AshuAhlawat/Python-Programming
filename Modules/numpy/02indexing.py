import numpy as np
arr0 = np.array([1, 2, 3, 4])

# 1-D array
# indexing the 1st element in an array
print(arr0[0])

# indexing the 2nd element of the array
print(arr0[1])

# adding two numbers from an array using thier index
print(arr0[2]+arr0[3])

# 2-D array
# indexing the 2nd element on 1st dim and 5th element on the 2nd dim
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on the 1st dim: ', arr1[0, 1])
print('5th element on the 2nd dim: ', arr1[1, 4])

# 3-D array
# access the third element of the 2nd array of the 1st array

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[0, 1, 2])
