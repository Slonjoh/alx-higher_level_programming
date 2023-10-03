#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            if i != 8 or j != 9:
                print("{:d}{:d}, ".format(i, j), end="")

print("{:d}{:d}".format(8, 9))
