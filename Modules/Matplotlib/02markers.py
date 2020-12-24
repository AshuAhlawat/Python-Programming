import numpy as np
import matplotlib.pyplot as plt

ypoints = np.array([3, 6, 1, 10])

plt.plot(ypoints, marker='*')
plt.show()

line_type = ['-', '--', '-.', ':']
color_type = ['r', 'g', 'b', 'c', 'k', 'm', 'w']

for _ in line_type:
    for i in color_type:
        print(eval("plt.plot(ypoints,'o{}{}')" .format(_, i)))
        plt.show()
