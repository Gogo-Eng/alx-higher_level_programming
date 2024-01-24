#!/usr/bin/python3
if __name__ == "__main__":
    add = __import__ ("3-infinite_add")
    print(dir(add))
    for d in dir(add):
        if not d.startswith("__"):
            print(d)
