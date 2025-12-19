import pandas as  pd

print(pd.__version__)

data = [100, 200, 300, 400, 500]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])
print(series)
print(series.loc["c"])
print(series.iloc[3])
print(series[ series < 250 ])
print(type(series))


calories = {"Day 1": 420, "Day 2": 380, "Day 3": 390}
series2 = pd.Series(calories)
print(series2)
print(series[series < 250])