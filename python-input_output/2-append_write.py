#!/usr/bin/python3
"""
Implements append_write
Functions:
    - append_write
"""


def append_write(file_name="", text=""):
    """
    Appends the specified content to the specified file
    Args:
        - file_name(str) - The name of the file to
        append to. If the file does not exist, it
        will be created.

        - text(str) - The text to append to the file

    Returns:
        - int - The number of characters written to the
        file
    """
    with open(file_name, 'a') as f:
        return f.write(text)
