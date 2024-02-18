#!/usr/bin/python3
"""Create claass MyList"""


class MyList(list):
    """print sorted list"""
    def print_sorted(self):
        print(sorted(self))
