#!/usr/bin/python3
""" a class which can be accessed """
import json


class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string to returns the JSON string representation"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Writes the string representation of an object of a class
            into a file
        '''
        file_name = cls.__name__ + ".json"

        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)

    @staticmethod
    def from_json_string(json_string):
        """from json string that returns the list of the JSON string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = Rectangle(3, 8)
        elif cls.__name__ == "Square":
            r2 = Square(5)
        r2.update(**dictionary)
        return (r2)
