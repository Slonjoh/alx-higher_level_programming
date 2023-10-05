#!/usr/bin/python3

def magic_calculation(a, b):
    add = 0
    sub = 0

    if a < b:
        add = a + b
        for i in range(4, 6):
            add += add + i
        return (add)
    else:
        sub = a - b
        return (sub)
