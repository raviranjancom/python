import pandas as pd

df=pd.read_csv("data.csv", index_col="Name");
pokemon=input("Enter pokemon name : ")
try: 
    print(df.loc[pokemon])
except:
    print("Not Found")
