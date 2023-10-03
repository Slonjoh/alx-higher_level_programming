#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("{}".format("FizzBuzz"), end=" ")
        elif (x % 3 == 0):
            print("{}".format("Fizz"), end=" ")
        elif (x % 5 == 0):
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(x), end=" ")
