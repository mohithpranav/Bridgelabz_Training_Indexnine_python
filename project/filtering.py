import numpy as np

array = np.array([[1, 2, 3, 4,13, 32], [4, 5, 6, 34, 20, 19]])

print(array.ndim)

# Filter elements
seniors = array[(array > 19) & (array <= 65) ]
print(seniors)

#Replace elements
arr1 = np.where(array > 18, array, -1)
print(arr1)

arr2 = np.where(array > 14)
print(arr2)