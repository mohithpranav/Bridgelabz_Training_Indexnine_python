# Basic Functions
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# functions with default parameters
def greet(name, msg="Good morning"):
    print(f"{msg}, {name}!")

greet("Mohith")
greet("Pranav", "Good evening")

# Returning Multiple Values (using tuple)
def get_stats(nums):
    total = sum(nums)
    length = len(nums)
    avg = total / length if length > 0 else 0
    return total, avg

numbers = [10, 20, 30]
total, avg = get_stats(numbers)
print("Total:", total)
print("Average:", avg)

