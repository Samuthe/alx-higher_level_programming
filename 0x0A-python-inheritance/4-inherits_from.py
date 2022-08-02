#!/usr/bin/python3
"""Only subclass"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a_class
    inherited (directly or indirectly)
    from the specified class ; otherwise False"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
