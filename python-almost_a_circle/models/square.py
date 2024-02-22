#!/usr/bin/python3
"""Create class sqaure from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Private att size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set private att size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update att"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.width,  # Using width as size for a square
            'x': self.x,
            'y': self.y
        }
