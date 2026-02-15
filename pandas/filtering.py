import pandas as pd

df=pd.read_csv("data.csv");

tallpokemon=df[df["Height"]>=2.0]
heavypokemon=df[df["Weight"]>=4.0]
legendarypokemon=df[df["Legendary"]==1]
waterpokemon=df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
ff_pokemon=df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]
print(ff_pokemon)
