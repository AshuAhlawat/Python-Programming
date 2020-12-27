import pandas as pd
df = pd.read_csv('Python Programming\Modules\Pandas\data.csv')
# print(df)
df1 = df.to_string()
# print(df1)

# analyzing
print(df.head(3))
print(df.head())
print(df.tail())
print(df.info())
