#!/usr/bin/python3

"""Define a class square"""
class Square:

    """Initialize class square with .__size attribute set to 0"""
    def __init__(self, size=0):

        """if type size is not an int, raise a type error"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

            """size must be greater than 0, else, ValueError is raised with a message"""
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

                """otherwise, set it to size"""
            else:
                self.__size = size

