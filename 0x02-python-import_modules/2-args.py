#!/usr/bin/python3
import sys

argv = sys.argv[1:]
argc = len(argv)

txt_arguments = 's' if argc != 1 else ''
end_string = ':' if argc > 0 else '.'

if __name__ == '__main__':
    print('{} argument{}{}'.format(argc, txt_arguments, end_string))

    if argc == 0:
        exit(0)

    for i, arg in enumerate(argv, start=1):
        print('{}: {}'.format(i, arg))
