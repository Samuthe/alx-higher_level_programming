#!/usr/bin/python3


class Base:
    """New class"""

    """private class attr/variable"""
    __nb_objects = 0

    def __init__(self, id=None):
        """if id is not None, assign the public instance 
        attribute id with this argument value"""
        if id is not None:
            self.id = id

            """otherwise, increment __nb_objects and assign the 
            new value to the public instance attribute id"""
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
