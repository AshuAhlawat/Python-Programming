from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# a - shape parameter.
# size - The shape of the returned array.

x = random.pareto(a=2, size=(2, 3))
print(x)

sns.distplot(x)
plt.show()
