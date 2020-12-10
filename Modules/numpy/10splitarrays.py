import numpy as np

# spliting an array and make it 3 array and access it
arr0 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr0, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# splitimg 2-D arrays
arr1 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr1, 3, axis=1)
print(newarr)

hnewarr = np.hsplit(arr1, 2)
print(hnewarr)

vnewarr = np.vsplit(arr1, 2)
