#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """define a square"""
    def __init__(self, size=0):

        """The format of parameter is:
        name (square): description
        Square is a class type for create a square"""

        """Args:
        param1 (size): the first parameters"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """Return square area"""
        return(self.__size * self.__size)
