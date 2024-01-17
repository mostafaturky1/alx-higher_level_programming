#!/usr/bin/python3
"""Defines a rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
