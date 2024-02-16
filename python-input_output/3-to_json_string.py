#!/usr/bin/python3
"""define a function that return the json format of an object"""


import json


def to_json_string(my_obj):
    """Return the json format"""
    return (json.dumps(my_obj))
