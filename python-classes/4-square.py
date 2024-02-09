#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        self.__size = size

    """The format of parameter is:
        name (square): description
        Square is a class type for create a square"""

    """Args:
        param1 (size): the first parameters
        param2 (area): the second parameters for calculate the area"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
