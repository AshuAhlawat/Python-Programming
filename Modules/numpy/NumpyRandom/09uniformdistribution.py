from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# a - lower bound - default 0 .0.

# b - upper bound - default 1.0.

# size - The shape of the returned array.

x = random.uniform(size=(2, 3))
sns.distplot(x, hist=False)
plt.show()

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()
