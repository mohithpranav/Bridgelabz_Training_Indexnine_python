# scalar arthmetic operations
import numpy as np

array = np.array([10, 20, 30, 40, 50.8, 60.3])

print(array + 5)  # Adds 5 to each element: [15, 25, 35, 45]
print(array - 2)  # Subtracts 2 from each element: [8, 18, 28, 38]
print(array * 3)  # Multiplies each element by 3: [30, 60, 90, 120]
print(array / 10) # Divides each element by 10: [1., 2., 3., 4.]
print(array ** 2) # Squares each element: [100, 400, 900, 1600] 
print(array % 7)  # Modulus of each element by 7: [3, 6, 2, 5]

print(np.sqrt(array))  # Square root of each element: [3.16227766, 4.47213595, 5.47722558, 6.32455532]
print(np.round(array))  # rounds to the nearest integer
print(np.floor(array)) # rounds down to the nearest integer
print(np.ceil(array)) # rounds up to the nearest integer


# vector arithmetic operations
radii = np.array([1, 2, 3, 4])

print(np.pi * radii ** 2 )

# element-wise operations
array1 =  np.array([1, 2, 3, 4])
array2 =  np.array([5, 6, 7, 8])
print(array1 + array2)  # Element-wise addition: [6, 8, 10, 12]
print(array1 - array2)  # Element-wise subtraction: [-4, -4, -4, -4]
print(array1 * array2)  # Element-wise multiplication: [5, 12, 21, 32]
print(array1 / array2)  # Element-wise division: [0.2, 0.3333, 0.4286, 0.5]
print(array1 ** array2) # Element-wise exponentiation: [1, 64, 2187, 65536]
print(np.dot(array1, array2)) # Dot product: 70


# comparation operations
array1 = np.array([10, 20, 30, 40])
print(array1 > 25)  # [False, False, True, True]
print(array1 < 25)  # [True, True, False, False]

array1[array1 > 25] = 99
print(array1)  # [10, 20, 99, 99]
 