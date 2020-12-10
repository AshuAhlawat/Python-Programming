import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

filter_array=[]

for i in arr:
    if i>42:
        filter_array.append(True)
    else:
        filter_array.append(False)
newarr=arr[filter_array]

print(filter_array)
print(newarr)

arr1=np.array([1,2,3,4,5,6,7])
fil_arr1=arr1%2==0
newarr=arr1[fil_arr1]

print(fil_arr1)
print(newarr)