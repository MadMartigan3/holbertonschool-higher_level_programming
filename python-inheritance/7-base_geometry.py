#!/usr/bin/python3
"""defines class BaseGeomtry
with public instance methods for area and integer validation"""


class BaseGeometry:
    """class with public instance"""
    def area(self):
        """Raise exception for area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
