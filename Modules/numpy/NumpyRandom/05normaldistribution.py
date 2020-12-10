from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(3, 5))

print(x)

# This normal func uses 3 parameters

# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

y = random.normal(loc=1, scale=2, size=(2, 3))

print(y)


sns.distplot(random.normal(size=1000), hist=False)

plt.show()
