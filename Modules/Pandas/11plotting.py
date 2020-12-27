import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Python Programming\Modules\Pandas\datacleaningdemo.csv')

df.plot(kind='scatter',x='Duration',y='Calories')
plt.show()

df.plot(kind='hist',x='Duration',y='Maxpulse')
plt.show()