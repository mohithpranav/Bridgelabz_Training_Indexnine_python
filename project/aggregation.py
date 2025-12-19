import pandas as pd


df = pd.read_csv("data.csv")
# print(df)

# Whole Dataframe
# print(df.sum(numeric_only=True))
# print(df.mean(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.count())

# single column
# print(df["Height"].sum())
# print(df["Weight"].mean())
# print(df["Height"].count())

group_hight = df.groupby("Type1")
grp_2 = df.groupby("Type2")

print(group_hight["Height"].sum())
print(grp_2["Weight"].max())