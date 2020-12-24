import numpy as np
import matplotlib.pyplot as plt

x = np.array([12, 23, 43, 35])
labels = ["A", "B", "C", "D"]
myexplode = [0.1, 0.1, 0, 0.1]

plt.pie(x, labels=labels, startangle=90, explode=myexplode, shadow=True)
plt.legend(title="PIE CHART")
plt.show()
