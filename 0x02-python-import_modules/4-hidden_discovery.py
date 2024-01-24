#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for run in dir(hidden_4):
        if not run.startswith("_"):
            print("{}".format(run))
