import pandas as pd

df=pd.read_csv("data.csv", index_col="Name")

# selectin by column
# print(df["Name"])
# print(df["Height"])
# print(df["Weight"])

# selection by multiple column
# print(df[["Name", "Height", "Weight"]])

# selection by row
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]]) 


#Access by integer index
print(df.iloc[0:11:2, 0:3])
