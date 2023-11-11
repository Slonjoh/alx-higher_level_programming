#!/usr/bin/python3
"""
Square class inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes to the instance."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def to_csv(self):
        """Return a list representing the instance for CSV serialization."""
        return [self.id, self.size, self.x, self.y]
