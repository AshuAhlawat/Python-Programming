import numpy as np

arr0 = np.array([1, 2, 3, 5, 4, 6, 7, 8])
x = np.where(arr0 == 4)
# returns the index of the number and the dtype
print(x)

even = np.where(arr0 % 2 == 0)  # returns the index of the even numbers
odd = np.where(arr0 % 2 == 1)  # returns the index of the odd numbers
print(even)
print(odd)

y = np.searchsorted(arr0, 5)
print(y)

z= np.searchsorted(arr0,[4,5,6], side='right')
print(z)
