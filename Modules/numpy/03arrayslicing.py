import numpy as np
# 1-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[2:])
print(arr[-3:-1])
print(arr[::2])

# 2-D array
arr1 = np.array([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]])
print(arr1[1, 1:4])
print(arr1[0:3, 1:5])
