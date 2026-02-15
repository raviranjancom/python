import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# working with pandas and matplotlib

df=pd.read_csv("data.csv")
type_count=df["Type1"].value_counts(ascending=True)
plt.title("Pokemon")
plt.barh(type_count.index,
        type_count.values,
        color="tomato"
        )
plt.show()
