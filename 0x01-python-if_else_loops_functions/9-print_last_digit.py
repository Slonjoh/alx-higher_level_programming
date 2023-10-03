#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    last_digit_str = str(last_digit).zfill(2)
    print(last_digit_str)
    return last_digit_str
