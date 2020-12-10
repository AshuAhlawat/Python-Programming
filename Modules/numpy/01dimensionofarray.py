import numpy as np

# 0D array
arr0 = np.array(42)
print(arr0)

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2-D array
arr2 = np.array([[1, 2, 3], [5, 6, 7]])
print(arr2)

# 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

# check the dimension
a = np.array(43)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [5, 6, 7]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# printing a nth dimensions array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions: ', arr.ndim)
