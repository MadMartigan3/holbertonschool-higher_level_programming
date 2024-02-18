#!/usr/bin/python3
"""Create a class Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Representation json of student class"""
        return (self.__dict__)
