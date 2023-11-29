#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if (n // 5) * 5 == n and (n // 3) * 3 == n:
            print("FizzBuzz", end=" ")
        elif (n // 3) * 3 == n:
            print("Fizz", end=" ")
        elif (n // 5) * 5 == n:
            print("Buzz", end=" ")
        else:
            print(n, end=" ")
