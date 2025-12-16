import numpy as np

print(np.__version__)

my_list = [1,2,3,4]

print(my_list * 2) # This will concatenate the list with itself
print(my_list)  # Original list remains unchanged

array = np.array([1,2,3,4]) 
print((array) * 2) # This will multiply each element by 2


array1 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                    [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
                    [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'a']]])

print(array1.shape) # Prints the shape of the array - (3, 3, 3) (3 layers, 3 rows, 3 columns)
print(array1.ndim) # Prints the number of dimensions - 3

word = array1[0,0,0] + array1[2, 0, 0] + array1[2, 2, 0]
print(word)


# slicing  array[start: end: step]
nums = np.array([[1,2,3], 
                 [4,5,6], 
                 [7,8,9], 
                 [10,11,12]])

print(nums[0]) #[1,2,3]
print(nums[1:3]) # [[4,5,6], [7,8,9]]
print(nums[0:4:2]) # [[1,2,3], [7,8,9]]
print(nums[::-1]) # Reverses the array

#
print(nums[:, 2]) # Prints all rows in the 3rd column: [3,6,9,12]
print(nums[:, 1:3]) # Prints all rows in the 2nd and 3rd columns: [[2,3], [5,6], [8,9], [11,12]]

print(nums[1:3, 0:2]) # Prints rows 2 and 3, columns 1 and 2: [[4,5], [7,8]]