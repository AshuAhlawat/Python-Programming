import pandas as pd

deta = {
    "names": ["ashu", "ankit", "gaurav", "dingo"],
    "hours": [10, 18, 14, 6]
}
myvar = pd.DataFrame(deta)
print(myvar)

df = pd.DataFrame(deta, index=["noob", "noober", "noobest", "The God"])
print(df.loc[["noob"]])
print(df.loc[["noob", "noobest"]])
