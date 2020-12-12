import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])


operaions=['add','subtract','multiply','divide','divmod']
for i in operaions:
    print(eval('np.{}(arr1,arr2)'.format(i)))