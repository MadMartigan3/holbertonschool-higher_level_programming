#!/usr/bin/python3
"""define a function that return the json format of an object"""


import json


def save_to_json_file(my_obj, filename):
    """Write into filenaame"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
