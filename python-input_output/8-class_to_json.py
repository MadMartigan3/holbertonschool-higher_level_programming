#!/usr/bin/python3
"""Write a function that returns the dictionary
description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """Return dictionnary desc of obj"""
    return (obj.__dict__)
