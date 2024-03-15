#!/usr/bin/python3
"""
Implements the load_from_json_file function
Functions:
    - load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Returns the object represented by the JSON in the
    specified file.

    Args:
        - filename(str) - The name of the file that
        contains the JSON
    Returns:
        - Object - The object represented by the JSON
        in the specified file
    """
    with open(filename) as f:
        return json.load(f)
