#!/usr/bin/python3
"""define a function that create the json format of an object"""
import json


def load_from_json_file(filename):
    """create an object"""
    with open(filename) as file:
        return (json.load(file))
