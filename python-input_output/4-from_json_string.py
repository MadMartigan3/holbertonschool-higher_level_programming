#!/usr/bin/python3
"""define a function that return the json format of an object"""


import json


def from_json_string(my_str):
    """Return the json format"""
    return (json.loads(my_str))
