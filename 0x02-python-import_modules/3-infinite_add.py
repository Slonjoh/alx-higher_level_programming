#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]  # Exclude the script name from the list

    result = 0

    for arg in args:
        result += int(arg)

    print(result)
