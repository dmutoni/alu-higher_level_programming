#!/usr/bin/python3
"""
Implements the inherits_from function
Functions:
    - inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance
    of a class that inherits from the
    specified class
    """
    obj_class = type(obj)
    is_sub_class = issubclass(obj_class, a_class)
    return is_sub_class and obj_class != a_class
