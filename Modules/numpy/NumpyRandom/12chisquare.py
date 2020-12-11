from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# df - (degree of freedom).

# size - The shape of the returned array.

x = random.chisquare(df=2, size=(2, 3))
print(x)

sns.distplot(x)
plt.show()
