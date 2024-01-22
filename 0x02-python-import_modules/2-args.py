#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    length = len(argv)

    if length == 1:
        print(f"{length - 1:d} arguments.")
    else:
        numbering = 1
        if length == 2:
            print(f"{(length - 1):d} argument:")
        else:
            print(f"{length - 1:d} arguments:")
        for i in argv:
            if i is not argv[0]:
                print(f"{numbering:d}: {i:s}")
                numbering += 1
