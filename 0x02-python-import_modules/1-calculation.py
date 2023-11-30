#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(int(a), int(b))))
    print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
    print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    print("{} / {} = {}".format(a, b, div(int(a), int(b))))

