#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(number))
    for i in range (number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
