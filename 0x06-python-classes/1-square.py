#!/usr/bin/python3

"""a class Square that defines a square by:
   Private instance attribute: size
   Instantiation with size (no type/value verification)
   You are not allowed to import any module"""


class Square:
    """Class Square"""
    def __init__(self, size):
        """A private instance attribute size"""
        self.__size = size
