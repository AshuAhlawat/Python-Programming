# NumPy provides functions to perform log at the base 2, e and 10.

# We will also explore how we can take log for any base by creating a custom ufunc.

# All of the log functions will place -inf or inf in the elements if the log can not be computed.

import numpy as np

arr=np.arange(1,10) # making an array starting from 1 to 10(excluded)
print(arr)

print(np.log2(arr)) #log base 2
print(np.log(arr)) # log base e
print(np.log10(arr))# log base 10

from math import log

nplog=np.frompyfunc(log,2,1)
print(nplog(int(input('Enter the value of the number: ')),int(input("Enter the Base: "))))