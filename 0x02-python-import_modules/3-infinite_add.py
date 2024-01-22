#!/usr/bin/python3

from sys import argv


def add():
    length = len(argv)
    adds = 0

    if length == 1:
        return (0)
    elif length == 2:
        return int(argv[1])
    else:
        for i in argv:
            if i is not argv[0]:
                adds += int(i)
        return int(adds)


result = add()
print(result)
