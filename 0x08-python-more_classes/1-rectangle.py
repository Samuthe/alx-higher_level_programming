#!/usr/bin/python3

"""class Rectangle initialization"""
class Rectangle:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

        """initialize my class object property of width"""
        @property
        def width(self):
            return (self.__width)

            """"define property setter of width"""
            @width.setter
            def width(self, value):
                if type(value) != int:
                    raise TypeError("width must be an integer")
                if value < 0:
                    raise ValueError("width must be >= 0")
                self.__width = value

                """class property of height"""

                @property
                def height(self):
                    return (self.__height)

                    """define property setter of height"""
                    @height.setter
                    def height(self, value):
                        if type(value) != int:
                            raise TypeError("height must be an integer")
                        if value < 0:
                            raise ValueError("height must be >= 0")
                        self.__height = value


