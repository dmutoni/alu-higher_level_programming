#!/usr/bin/python3
"""
Implements the is_kind_of_class function
Functions:
    - is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a_class
    Or is an instance of a superclass of a_class
    Args:
        - obj(Object) - The object to check
        - a_class(Class) - The class to compare against
    Returns:
        - bool - True if obj is an instance of a_class
        or obj is an instance of a superclass of a_class
    """
    is_class = type(obj) == a_class
    is_sub_class = issubclass(type(obj), a_class)
    return is_class or is_sub_class
