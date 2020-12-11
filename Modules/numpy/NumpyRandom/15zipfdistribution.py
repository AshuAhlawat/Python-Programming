from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# a - distribution parameter.

# size - The shape of the returned array.

x=random.zipf(a=2,size=(2,3))
print(x)

sns.distplot(x)
plt.show()