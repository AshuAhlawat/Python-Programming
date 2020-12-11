from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

# size - The shape of the returned array.

x = random.exponential(scale=2, size=(2, 3))
print(x)

sns.distplot(x, hist=False)
plt.show()
