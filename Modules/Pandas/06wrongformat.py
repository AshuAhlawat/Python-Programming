import pandas as pd

df = pd.read_csv('Python Programming\Modules\Pandas\datacleaningdemo.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

df.dropna(subset=["Date"], inplace=True)

print(df.to_string())