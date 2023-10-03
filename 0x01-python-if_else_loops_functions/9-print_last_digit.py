#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulo
    print(last_digit)  # Print the last digit
    return last_digit  # Return the value of the last digit
