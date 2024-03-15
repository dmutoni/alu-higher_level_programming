#!/usr/bin/python3
"""
Implements the to_json_string function
Functions:
    - to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Serialises an object to JSON
    Args:
        - my_obj(Object) - The object to serialise
    Returns:
        - str - The serialised JSON
    """
    return json.dumps(my_obj)
