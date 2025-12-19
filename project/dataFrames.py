import pandas as  pd

data = {
    "Name": ["Spongebob", "patrick", "Squidward"],
    "Age": [30, 35, 40]
}

df = pd.DataFrame(data, index=["a", "b", "c"])
print(df)

# add new column
df["job"] = ["Cook", "Unemployed", "Cashier"]
print(df)


print("--------------")
# add new row
new_row = pd.DataFrame([{"Name": "sanhok", "Age": "30", "job":"Developer"}, {"Name": "Vikas", "Age": "20", "job":"employee"}], index=["d", "e"])
print(pd.concat([df, new_row]))