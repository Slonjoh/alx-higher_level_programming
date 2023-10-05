#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    if ac == 1:
        print("{} arguments.".format(ac - 1))
    elif ac == 2:
        print("{} argument:".format(ac - 1))
        for x in range(1, ac):
            print("{}: {}".format(x, sys.argv[x]))
    else:
        print("{} arguments:".format(ac - 1))
        for x in range(1, ac):
            print("{}: {}".format(x, sys.argv[x]))
