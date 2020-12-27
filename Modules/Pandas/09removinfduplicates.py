import pandas as pd

df = pd.read_csv('Python Programming\Modules\Pandas\datacleaningdemo.csv')

print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df)