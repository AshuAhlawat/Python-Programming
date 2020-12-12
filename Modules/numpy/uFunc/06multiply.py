import numpy as np

arr1=np.arange(1,6)
arr2=np.arange(1,11,2)
print(arr1)
print(arr2)

newarr=np.prod(arr1)
print(newarr)

newarr=np.prod([arr1,arr2])
print(newarr) # returns an integar

newarr=np.prod([arr1,arr2],axis=1)
print(newarr)

newarr=np.cumprod(arr1)
print(newarr)