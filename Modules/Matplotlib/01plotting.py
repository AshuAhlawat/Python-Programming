import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1, 1, 5.5, 3, 8, 5, 6, 1])
ypoints = np.array([76, 65, 23, 24, 6, 54, 33, 76])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([1, 2, 3, 4, 5, 6, 7])
ypoints = np.array([21, 43, 56, 1234, 222, 576, 54])

plt.plot(xpoints, ypoints, 'o')
plt.show()

plt.plot(ypoints)
plt.show()
