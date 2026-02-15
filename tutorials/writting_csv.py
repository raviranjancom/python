import os
import csv

data=[
    ["Name", "age", "job"],
    ["Ravi Ranjan",21,"pentester"],
    ["Mr Robot",23,"developer"],
    ["bluegamerz",19,"gamer"]
]
path="output.csv"

try:
    with open(path,"w",newline="") as file:
        writer=csv.writer(file)
        for row in data:
            writer.writerow(row)
        print("succesfully written")

except Exception:
    print("something went wrong!")

