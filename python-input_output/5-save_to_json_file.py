#!/usr/bin/python3
"""
Implements the save_to_json_file function.
Functions:
    - save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves the specified object to the specified file.
    The object is encoded in JSON first

    Args:
        - my_obj (Object) - The object to save
        - filename (str) - The filename to write to

    Returns:
        - None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
