#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print((self.__position[0]) * " ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for i in range(len(value)):
            if value[i] < 0:
                raise TypeError("must be a tuple of 2 positive integers")
