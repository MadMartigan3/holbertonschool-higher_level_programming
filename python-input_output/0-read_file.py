#!/usr/bin/python3
"""define a function who read a text from a file"""


def read_file(filename=""):
    """Read text from a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
