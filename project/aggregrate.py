import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                    [7, 8, 9]])

print(array.ndim)
print(np.sum(array))         # Total sum of all elements: 45
print(np.mean(array))        # Mean of all elements: 5.0
print(np.std(array))         #  Standard deviation of all elements: 2.581988897471611
print(np.var(array))         # Variance of all elements: 6.666666666666667
print(np.max(array))        # Maximum element: 9
print(np.min(array))        # Minimum element: 1
print(np.argmax(array))      # Index of the maximum element (in flattened array): 8
print(np.argmin(array))      # Index of the minimum element (in flattened array): 0

print(np.sum(array, axis=0))  # Sum of each column: [12, 15, 18]
print(np.sum(array, axis=1))  # Sum of each row: [6, 15, 24]

