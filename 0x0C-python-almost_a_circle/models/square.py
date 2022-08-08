#!/usr/bin/python3


"""class square inherits Rectangle"""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, id, x, y)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
            self.__width = size
            self.__height = size

        
    def __str__(self):
        end_string = "[Square] "
        end_string = "({})".format(self.id)
        end_string = "{:d}/{:d} - ".format(self.x, self.y)
        end_string = "{:d}".format(self.size)
        return end_string

    def update(self, *args, **kwargs):
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

        if id in kwargs:
            self.id = kwargs["id"]
        if size in kwargs:
            self.size = kwargs["size"]
        if x in kwargs:
            self.x = kwargs["x"]
        if y in kwargs:
            self.y = kwargs["y"]

    

    """Rectangle instance to dictionary representation"""
    def to_dictionary(self):
        return{
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
