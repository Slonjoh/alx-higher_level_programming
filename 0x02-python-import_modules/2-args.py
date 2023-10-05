#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name itself
    args = argv[1:]  # Exclude the script name from the list

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
