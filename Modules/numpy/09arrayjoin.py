import numpy as np
from numpy.lib.shape_base import column_stack
# joining 2 arrays in 1
arr0 = np.array([1, 2, 3])
arr1 = np.array([4, 5, 6])
joined_arr = np.concatenate((arr0, arr1))
print(joined_arr)

# joining 2 2-D arrays
arr2 = np.array([[1, 2], [3, 4]])
arr3 = np.array([[5, 6], [7, 8]])
joined_arr1 = np.concatenate((arr2, arr3), axis=1)
print(joined_arr1)

# stacking 2 arrays

arr4 = np.array([1, 2, 3])
arr5 = np.array([4, 5, 6])
# normal stacking
stacked = np.stack((arr4, arr5), axis=1)
print(stacked)
# stacking row wise
rowstacked = np.hstack((arr4, arr5))
print(rowstacked)
# stacking column wise
columnstacked = np.vstack((arr4, arr5))
print(columnstacked)
# stacking along height
depthstacked = np.dstack((arr4, arr5))
print(depthstacked)
