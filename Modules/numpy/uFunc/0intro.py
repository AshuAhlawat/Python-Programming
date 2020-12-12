# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

# ufuncs also take additional arguments, like:

# where boolean array or condition defining where the operations should take place.

# dtype defining the return type of elements.

# out output array where the return value should be copied.




#using built-in method
x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)


#using uFunc method
import numpy as np
m=[2,3,4,6]
n=[10,11,12,13]
o=np.add(m,n)
print(o)