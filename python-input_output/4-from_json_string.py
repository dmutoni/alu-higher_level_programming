#!/usr/bin/python3
"""
Implements the from_json_string
Functions:
    - from_json_string
"""
import json


def from_json_string(my_str):
    """
    Reads a json_string and returns the object
    Args:
        - my_str (str) - The string to parse
    Returns:
        - Object - The Python object represented
        by the string
    """
    return json.loads(my_str)
