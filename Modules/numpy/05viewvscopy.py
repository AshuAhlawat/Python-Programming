# Copy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()  # copying the array
arr[0] = 40  # indexing the value of 1st element 40

print(arr)  # output=[40 2 3 4 5]
print(x)  # output=[1 2 3 4 5]
# View
arr1 = np.array([3, 4, 5, 6, 7, 8])
y = arr1.view()
print(y)
arr1[0] = 42
print(arr1)

arr2 = np.array([12, 11, 14, 13, 15])
n = arr2.copy()
n[1]=13
m = arr2.view()
m[4]=20
print(n.base)
print(m.base)
