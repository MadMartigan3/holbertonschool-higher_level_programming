#!/usr/bin/python3
"""define a function to append a text"""


def append_write(filename="", text=""):
    """Return the len of the text"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

        return len(text)
