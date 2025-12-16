import numpy as np

# Broadcasting example
array1 = np.array([[1, 2, 3],
                  [4, 5, 6]])
array2 = np.array([10, 20, 30])
array3 = np.array([[100],
                   [200], [300]])

print(array1.shape)  # (2, 3)
print(array2.shape)  # (3,)
print(array3.shape)  # (3, 1)

print(array1 + array3)  # Broadcasting addition