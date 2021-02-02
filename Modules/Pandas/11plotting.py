import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Coding\economy.csv')

df.plot(kind='scatter')
plt.show()

# df.plot(kind='hist')
# plt.show()