#!/usr/bin/python3
"""
Implements a square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square - represents a square
    methods:
        - area() - returns the area
    """
    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2
