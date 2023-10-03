#!/usr/bin/python3

combinations = []

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit != second_digit:
            combinations.append("{:d}{:d}".format(first_digit, second_digit))

print(", ".join(combinations))
