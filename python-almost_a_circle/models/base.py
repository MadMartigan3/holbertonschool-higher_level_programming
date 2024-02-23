#!/usr/bin/python3
"""Define a class Base"""
import json


class Base():
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init Id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return representation json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write in the json file the representation"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of json string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return dummy_instance"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """Return list of json load"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                instances = [cls.create(**dic) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return ([])
