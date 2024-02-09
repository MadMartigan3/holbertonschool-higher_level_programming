#!/usr/bin/python3

"""Creates a class Rectangle"""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """The format of parameter is:
        name (rectangle): description
        Rectangle is a class type for create a rectangle"""

        """Args:
        param1 (width): the first parameters
        param2 (height): the second parameters"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
