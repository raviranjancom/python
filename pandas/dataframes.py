import pandas as pd

data={"Name": ["Spongebob", "patrick", "crabby", "Doraemon"], "Age": [21, 28, 19, 16]};
df=pd.DataFrame(data,index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"]);

print(df.loc["Employee 1"]);
print(df.iloc[0]);

# creating row for Dataframes
df["Job"]=["Cook", "Waiter", "Manager","N/A"]
print(df);

# adding new row
print("New Row : -------------")
new_row=pd.DataFrame([{"Name": "Sandy", "Age": 23, "Job":"Waiter"}, {"Name": "Eugene", "Age": 60, "Job": "Marketing Head"}], index=["Employee 5", "Employee 6"])
df=pd.concat([df,new_row]);
print(df)
