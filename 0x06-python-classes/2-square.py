#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square with a given size."""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
