import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 4])

plt.bar(x, y, width=0.5, color="yellow")
plt.show()

plt.barh(x, y, height=0.7, color='blue')
plt.show()
