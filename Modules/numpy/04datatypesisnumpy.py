import numpy as np
arr = np.array([1, 2, 4, 5])
print(arr.dtype)

arr1 = np.array(['ashu', 'silver', 'anky', 'dingo'])
print(arr1.dtype)

# making data type in numoy array
arr2 = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr2)
print(arr2.dtype)

arr3 = np.array([1, 2, 3, 4, 5, 6], dtype='i4')
print(arr3)
print(arr3.dtype)

# new array from older array
arr4 = np.array([1.1, 2.5, 3.6])
newarr = arr4.astype('i')
print(newarr)
print(newarr.dtype)

arr5 = np.array([90, 12, 23, 34, 0])
newarr1 = arr5.astype(int)
print(newarr1)
print(newarr1.dtype)
newarr1 = arr5.astype(bool)
print(newarr1)
print(newarr1.dtype)
