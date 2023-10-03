def islower(c):
    # Check if the ASCII value of 'c' is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Test cases
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
print(islower('0'))  # False
