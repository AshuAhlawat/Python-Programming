from textwrap import shorten
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2, 3))
print(x)

sns.distplot(x, kde=False)
plt.show()
