#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    length = len(argv)

    if length == 1:
        print(f"{length - 1} arguements")
    else:
        numbering = 1
        print(f"{length - 1} arguements")
        for i in argv:
            if i is not argv[0]:
                print(f"{numbering}: {i:s}")
                numbering += 1
