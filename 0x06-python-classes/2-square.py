#!/usr/bin/python3

"""a class Square that defines a square by:
     Private instance attribute: size
     Instantiation with optional size: def __init__(self, size=0):
       size must be an integer, otherwise raise a TypeError exception
       if size is less than 0, raise a ValueError exception"""


class Square:
    """A square class"""
    def ___init___(self, size=0):
        """Class Instance"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
