#!/usr/bin/python3

def islower(c):
    # Check if the character 'c' is lowercase
    return ord('a') <= ord(c) <= ord('z')

# Test cases
print(islower("a"))  # True
print(islower("A"))  # False
print(islower("z"))  # True
print(islower("Z"))  # False
print(islower("0"))  # False

# Additional test cases
print(islower("4"))  # False
print(islower("!"))  # False
print(islower(4))    # False
print(islower("H"))  # False

# Check for non-alphabet characters
if islower("a"):
    print("'a' => lower")
elif islower("A"):
    print("'A' => upper")
elif islower("4"):
    print("'4' => upper")
elif islower("!"):
    print("'!' => upper")
else:
    print("Not a letter")

# Check for non-string input
try:
    islower(4)
except TypeError:
    print("TypeError: islower() argument must be a string of length 1")
