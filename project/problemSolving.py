# two sum
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in num_map:
            return (num_map[need], i)
        
        num_map[num] = i
    print(num_map) # {2: 0, 7: 1, 11: 2, 15: 3}
    
print(two_sum([2, 7, 11, 15], 9))  # Output: (0, 1)


# reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"


# palindrome check
def is_palindrome(s):
    return s == s[::-1]