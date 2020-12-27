import pandas as pd

df = pd.read_csv('Python Programming\Modules\Pandas\datacleaningdemo.csv')

df.loc[7,"Duration"]=45

print(df)

for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.loc[x,"Duration"]=120

print(df.to_string())

#remoiving the row

for x in df.index:
    if df.loc[x,"Duration"]>120:
        df.drop(x,inplace=True)
print(df.to_string())