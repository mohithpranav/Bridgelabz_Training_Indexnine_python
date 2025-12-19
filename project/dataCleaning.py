import pandas as pd

df = pd.read_csv("data.csv")

# Data Cleaning - it is the process of fixing or removing incorrect, corrupted,
# incorrectly formatted, duplicate, or incomplete data within a dataset.
# 75 percent of work done in python is data cleaning

# drop irrelevent column 
print(df.drop(columns=["Legendary", "No"]))


# Handling missing data
print(df.dropna(subset="Type2"))
print(df.fillna({"Type2" : "None"}))

#fix inconsistent values
print(df["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE"}))

# standardize text
print(df["Name"].str.lower())

#Fix data type
df["Legendary"] = df["Legendary"].astype(bool)

print(df.to_string())



#remove duplicate
print(df.drop_duplicates().to_string())