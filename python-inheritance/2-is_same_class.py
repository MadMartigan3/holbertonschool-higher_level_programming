#!/usr/bin/python3
"""Define function is_same_class"""


def is_same_class(obj, a_class):
    """Return True if object is an instance of class"""
    if type(obj) is a_class:
        return True
    else:
        return False
