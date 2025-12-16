# Conditionals (if / elif / else)
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C or below"

print(f"Marks: {marks}, Grade: {grade}")

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")

# Loops (for / while)
languages = ["Python", "C++", "Java"]

for lang in languages:
    print(f"I know {lang}")

for i in range(1, 6):
    print(f"Number: {i}")
    
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
    

for i in range(1, 10):
    if i == 5:
        break        # stop loop completely
    if i % 2 == 0:
        continue     # skip even numbers
    print(i)         # prints odd numbers 1,3
