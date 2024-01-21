#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    length = len(argv)

    if length == 1:
        print("{:d} arguments.".format(length - 1))
    else:
        numbering = 1
        if length == 2:
            print(f"{(length - 1):d} argument:")
        else:
            print("{:d} arguments:".format(length - 1))
        for i in argv:
            if i is not argv[0]:
                print("{:d}: {:s}".format(numbering, i))
                numbering += 1
