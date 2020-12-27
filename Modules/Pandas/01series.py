import pandas as pd

a = [1, 4, 6]

myvar = pd.Series(a)
print(myvar)
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

studyhours = {"ashu": 10, "dingo": 6, "gaurav": 14, "anky": 18}
myvar = pd.Series(studyhours)
print(myvar)

myvar = pd.Series(studyhours, index=["ashu", "gaurav"])
print(myvar)
