from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
# lam - rate or known number of occurences e.g. 2 for above problem.

# size - The shape of the returned array.

x = random.poisson(lam=2, size=10)
sns.distplot(x)
plt.show()
