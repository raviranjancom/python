import pandas as pd

data=[100.1, 102, 103, 200, 202]
series=pd.Series(data)
print(series[series < 200])

calories={"day 1": 1750, "Day 2": 2100, "Day 3": 1700}
dict_series=pd.Series(calories);
print(dict_series);
