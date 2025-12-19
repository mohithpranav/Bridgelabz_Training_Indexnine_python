import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")


# selection by column
# print(df.index.to_series().to_string())
# print(df["Height"])
print(df[["Type1", "Type2"]])

# print by rows
print(df.loc["Pikachu"]) 
print(df.loc["Pikachu" : "Zubat", ["Height", "Weight"]])
print(df.iloc[0:11:3, 0:6 ])


pokaemon = input("Enter the pokemon name: ").title()
try:
    print(df.loc[pokaemon])
except KeyError:
    print(f"{pokaemon} doesn't exist")