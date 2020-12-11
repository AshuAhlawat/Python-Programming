from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# loc - mean, where the peak is. Default 0.

# scale - standard deviation, the flatness of distribution. Default 1.

# size - The shape of the returned array.

x = random.logistic(loc=1, scale=2, size=(2, 3))
sns.distplot(x, hist=False)
plt.show()

sns.displot(random.logistic(size=1000))
plt.show()
