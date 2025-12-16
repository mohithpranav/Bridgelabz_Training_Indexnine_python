# numbers 
a = 10  
b = -5 

pi = 3.14159

is_valid = True
result = a + b * pi
print("Result:", result)

# strings
name = "Mohith"
greeting = "hello," + name + "!"
print(greeting)

age = 21
test = "Mohith"
print(test[0])  # M
print(test[1: 4])  # ohi
print(test[::-1])  # htimoH


# lists (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'date']

for fruit in fruits:
    print(fruit)
    
# tuples (immutable, ordered)\
point = (2, 3)
x, y = point # unpacking
print("X:", x, "Y:", y)
# point[0] = 100   This will raise an error(tuple cannot be changed)

#Dictionaries (mutable, unordered), key value pairs
students = {
    "name": "Mohith",
    "age": 21,
    "courses": ["Math", "Science", "Art"]
}

print(students["name"])  # Mohith
print(students.get("branch", "CSE"))  # 21

students["college"] = "SRM"
students["age"] = 22
print(students) # {'name': 'Mohith', 'age': 22, 'courses': ['Math', 'Science', 'Art'], 'college': 'SRM'}

for key, value in students.items():
    print(key, ":", value)
    
# sets (mutable, unordered, no duplicates)
nums = {1, 2, 3, 4, 5}
print(nums)  # {1, 2, 3, 4, 5}

nums.add(6)
nums.remove(3)
print(nums)  # {1, 2, 4, 5, 6}


# None (absence of value)
result = None

if result is None:
    print("No result found")
    
    
#  Array 
import array as arr
numbers = arr.array('i', [1, 2, 3, 4, 5])
numbers.append(6)