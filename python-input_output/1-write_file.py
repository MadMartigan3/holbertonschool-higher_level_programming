#!/usr/bin/python3
"""define a function to write a text"""


def write_file(filename="", text=""):
    """Return the len of the text"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

        return len(text)
