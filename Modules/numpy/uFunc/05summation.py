import numpy as np

arr1=np.arange(1,6)
arr2=np.arange(1,11,2)
print(arr1)
print(arr2)

newarr=np.add(arr1,arr2)
print(newarr)

newarr=np.sum([arr1,arr2])
print(newarr)

#sumamtion of each array

newarr=np.sum([arr1,arr2],axis=1)
print(newarr)

# Cummulative sum means partially adding the elements in array.

# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

# Perfom partial sum with the cumsum() function.
newarr=np.cumsum(arr1)
print(newarr)