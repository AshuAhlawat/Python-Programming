import numpy as np
arr=np.array([1,2,3,4])
for x in arr:
    print(x)
arr1=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr1:
    for y in x:
        print(y)
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr2:
    for y in x:
        for z in y:
            print(z)
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr3):
    print(x)

arr4=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr4[:,::2]):
    print(x)

arr5=np.array([1,2,3])
for idx,x in np.ndenumerate(arr5):
    print(idx,x)

arr6=np.array([[1,2,3,4],[5,6,7,8]])
for idx,x in np.ndenumerate(arr6):
    print(idx,x)