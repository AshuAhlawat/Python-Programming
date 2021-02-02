import pandas as pd
df=pd.read_csv('D:\Coding\wiki.csv')
df.replace('"','')
df.to_csv('D:\Coding\wiki.csv')