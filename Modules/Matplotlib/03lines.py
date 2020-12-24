import numpy as np
import matplotlib.pyplot as plt

x1=np.array([3,2,5,7,9])
y1=np.array([6,7,13,21,14])
x2=np.array([3,2,5,7,9])
y2=np.array([5,8,21,2,4])

plt.plot(x1,ls=':',color='blue',linewidth='1.2',marker='4')
plt.plot(y1,ls='-',color='green',linewidth='1.2')

plt.show()

plt.plot(x1,y1,x2,y2)

plt.show()