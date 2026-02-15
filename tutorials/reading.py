import os
import csv

path="output.csv"

try:
    with open(path, "r") as file:
        content=csv.reader(file)
        for line in content:
            print(line[1])
except Exception:
    print("Could not read the file")
finally:
    pass
