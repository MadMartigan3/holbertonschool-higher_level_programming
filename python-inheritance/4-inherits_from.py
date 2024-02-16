#!/usr/bin/python3
"""Define function if object is an instance of class"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
