#!/usr/bin/python3

"""Implements a list with a print_sorted method
Classes:
    - MyList
"""


class MyList(list):
    """ Like a list but with a print_sorted method"""
    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
