import numpy as np
import matplotlib.pyplot as plt

x = np.array([12, 43, 1, 24, 5, 3, 6, 34, 645,
              43, 22, 44, 51, 57, 88, 65, 32, 34])
y = np.array([342, 4, 232, 34, 5, 4432, 465, 3345, 777,
              42, 4566, 123, 234, 345, 567, 678, 122, 223])

plt.scatter(x, y)
plt.show()
