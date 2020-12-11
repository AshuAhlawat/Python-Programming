from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# a - distribution parameter.

# size - The shape of the returned array.

x=random.zipf(a=2,size=1000)
sns.distplot(x[x<10],kde=False)
plt.show()