#!/usr/bin/python3
"""Defines a rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square instance."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update instance attributes with the provided arguments."""
        if len(args) == 0:
            for key, v in kwargs.items():
                self.__setattr__(key, v)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        def to_dictionary(self):
            """ to dictionary to return representation of a Square."""
            return {'id': self.id, 'x': self.x,
                    'size': self.size, 'y': self.y}
