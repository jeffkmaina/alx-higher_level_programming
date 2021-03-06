#!/usr/bin/python3
"""
Module 5-square
class Square
"""


class Square:
    """ Defines a square"""

    def __init__(self, size=0):
        """
        creates an instance of a Square

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """
        sets and gets the value of private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates area of square

        Args:
            size: size of square
        Returns:
            area of square
        """
        size = self.__size
        return (size * size)

    def my_print(self):
        """
        prints a square of size value using '#'
        """
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            print("#" * self.__size)
