# To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# 1. function - the name of the function.
# 2. inputs - the number of input arguments (arrays).
# 3. outputs - the number of output arrays.

import numpy as np

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)
res=myadd([1,2,3,4,5],[2,3,4,5,6])
print(res)

print(type(myadd))