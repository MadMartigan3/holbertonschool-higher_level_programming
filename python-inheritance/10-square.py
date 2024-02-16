#!/usr/bin/python3
"""Define class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for square inherits from rectangle"""
    def __init__(self, size):
        """init Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)
