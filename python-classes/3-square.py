#!/usr/bin/python3

"""Create a class Square"""


class Square:
    def __init__(self, size=0):

        """The format of parameter is:
        name (square): description
        Square is a class type for create a square"""

        """Args:
        param1 (size): the first parameters
        param2 (area): the second parameters for calculate the area"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return(self.__size * self.__size)
