import numpy as np

rgn = np.random.default_rng(seed=0)

print(rgn.integers(low = 0, high = 7))
print(rgn.integers(low = 0, high=7, size=(3,5)))
print(int(rgn.random() * 10))
print(rgn)


print(np.random.uniform(low = -1, high = 3, size=4))

