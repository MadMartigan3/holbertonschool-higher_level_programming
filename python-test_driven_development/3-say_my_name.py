#!/usr/bin/python3

"""function to divide a matrix"""


def say_my_name(first_name, last_name=""):
    """fonction that print a string

    Args:
    param1 (first_name): the first parameter
    param2 (last_name): the scd parameter
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
