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
        param2 (area): the second parameters for calculate the area
        param3 (my_print): the third parameters for print in stdout"""

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

    @property
    def position(self):
        """attribute position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """instance attribute position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """print in stdout the sqaure with #"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ",end="")
                for z in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
