#!/usr/bin/python3
"""Create claass MyList"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)