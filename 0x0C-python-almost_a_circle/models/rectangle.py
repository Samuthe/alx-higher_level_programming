#!/usr/bin/python3
"""imported Base class from base.py"""


from base import Base

"""class Rectangle extends Base class from base.py"""
class Rectangle(Base):
    
    """declaring the initials of Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Class property validation"""

    """1. find width-property and setter"""
    @property
    def width(self):
        """find width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be > 0")
            self.__width = value

    
    """2. find height-property and setter"""
    @property
    def height(self):
        """find/retrieve height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise ValueError("Value must be an integer")
        if value <= 0:
            raise TypeError("Value must be > 0")
            self.__height = value


    """3. find x-property and setter"""
    @property
    def x(self):
        """find/retieve x property"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise ValueError("Value must be an integer")
        if value <= 0:
            raise TypeError("Value must be >= 0")
            self.__x = value


     """4. find y-property and setter"""   
    @property
    def y(self):
        """find/retrieve y property"""
        return self.__y

    def y(self, value):
        if type(value) != int:
            raise ValueError("Value must be an integer")
        if value <= 0:
            raise TypeError("Value must be >= 0")
            self.__y = value

    """find the area of the rectangle"""
    def area(self):
        """area is height times width"""
        return self.height * self.width


    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for n in range(self.y):
            print()
        for i in range(self.height):
            for m in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Creates a string object from a given object"""
        end_string = "[Rectangle] "
        end_string += "({}) ".format(self.id)
        end_string += "{:d}/{:d} - ".format(self.x, self.y)
        end_string += "{:d}/{:d}".format(self.width, self.height)
        return end_string

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to each attribute"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]

        if "width" in kwargs:
            self.width = kwargs["width"]

        if "height" in kwargs:
            self.height = kwargs["height"]

        if "x" in kwargs:
            self.x = kwargs["x"]

        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """The dictionary representation Rectangle"""
        return 
        {
            "id": self.id, 
            "width": self.width, 
            "height": self.height,
                "x": self.x, 
                "y": self.y
                }



    

