#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()
    total = 0
    for item in my_list:
        if isinstance(item, int) and item not in unique_integers:
            unique_integers.add(item)
            total += item

    return total
