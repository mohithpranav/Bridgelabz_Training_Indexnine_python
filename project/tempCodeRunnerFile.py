import numpy as np

print(np.__version__)

my_list = [1,2,3,4]

print(my_list * 2) # This will concatenate the list with itself
print(my_list)  # Original list remains unchanged

array = np.array([1,2,3,4]) 
print((array) * 2) # This will multiply each element by 2


array1 = np.array([[['a', 'b', 'c'], ['d', 'e', 'f'], ],
                    [['j', 'k', 'l'], ['m', 'n', 'o'],],
                    [['s', 't', 'u'], ['v', 'w', 'x'],]])

print(array1.shape) # Prints the shape of the array - (3, 3, 3) (3 layers, 3 rows, 3 columns)