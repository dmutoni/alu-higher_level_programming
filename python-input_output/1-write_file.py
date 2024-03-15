#!/usr/bin/python3
"""
Implements write_file
Functions:
    - write_file
"""


def write_file(file_name="", text=""):
    """
    Writes the specified content to the specified file
    Args:
        - file_name(str) - The name of the file to
        write to. If the file already exists, its
        contents will be overwritten. If the file
        does not exist, it will be created.

        - text(str) - The text to write into the file

    Returns:
        - int - The number of characters written to the
        file
    """
    with open(file_name, 'w') as f:
        return f.write(text)
