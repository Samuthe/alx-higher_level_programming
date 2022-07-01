#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{} arguments".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{}".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(len(sys.argv[i])))
    else:
        print("{} arguments".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, len(sys.argv[i])))