#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nbr = len(sys.argv) - 1
    if nbr == 1:
        print("1 argument:")
    elif nbr == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(nbr))
    for i in range(nbr):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
