#!/usr/bin/python3
"""
Implements the is_same_class function
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of the specified class
    Args:
        - obj (Object) - The object to check
        - a_class(Class) - The class to compare with
    Returns:
        - Boolean - True if the object is an instance of the class
        and False if it is not
    """
    return type(obj) == a_class
