#!/usr/bin/python3
"""New class Geometry module"""


class BaseGeometry():
    """Base Geometry"""

    def area():
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} value must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} value must be greater than 0".format(name))
