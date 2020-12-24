import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 5, 7])
y = np.array([2, 4, 6, 8])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("GRAPH 1")

x1 = np.array([4, 6, 8, 10, 12])
y1 = np.array([3, 5, 7, 9, 11])

plt.subplot(1, 2, 2)
plt.plot(x1, y1)
plt.title("GRAPH 2")

plt.suptitle("GRAPHICAL REPRESENTATION")

plt.show()
