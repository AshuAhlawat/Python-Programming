import pandas as pd
df = pd.read_csv('Python Programming\Modules\Pandas\datacleaningdemo.csv')

df.dropna(inplace=True)

print(df.to_string())

df.fillna(130, inplace=True)

print(df.to_string())

df["Calories"].fillna(130, inplace=True)

x = df['Calories'].mean()
df['Calories'].fillna(x, inplace=True)

y = df['Calories'].median()
df['Calories'].fillna(y, inplace=True)

z = df['Calories'].mode()[0]  # [0] is the value that will be replaced
df['Calories'].fillna(z, inplace=True)
