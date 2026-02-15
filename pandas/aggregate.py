import pandas as pd

df=pd.read_csv("data.csv")

allData=df.max(numeric_only=True)
maxHeight=df["Height"].max(numeric_only=True)

group=df.groupby("Type1")
print(group["Height"].max())
