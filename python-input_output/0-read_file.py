#!/usr/bin/python3
"""
implements a read_file
Functions:
    - read_file
"""


def read_file(file_name=""):
    """
    Reads a specified file name and writes its contents
    to stdout
    Args:
        - file_name(str) - The name of the file to read
    Returns:
        - None
    """
    with open(file_name) as f:
        content = f.read()
        print(content, end="")
