import pandas as pd

df = pd.read_csv("data.csv")


# df[boolean_mask]
# Returns only rows where the mask is True
print(df[df["Height"] > 2])
print(df[df["Weight"] > 150])
print(df[df["Legendary"] == 1])

print("-----------------------Water--------------------")
print(df[df["Type1"] == "Water"])


print(df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")])

