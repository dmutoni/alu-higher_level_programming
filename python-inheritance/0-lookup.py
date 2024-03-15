#!/usr/bin/python3

"""
Lookup Module
Implements the lookup function.
Contains the following functions:
    * lookup - returns a list of all the attributes and methods of an object
"""


def lookup(obj):
    """ Returns a list of all the attributes and methods of an object
    Args:
        - obj(Object) The object whose properties will be returned
    Returns:
        - (List) list of all attributes
    """
    return dir(obj)
