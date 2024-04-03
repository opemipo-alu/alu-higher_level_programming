#!/usr/bin/python3
"""
This module contains the Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a size.

        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Getter method for __size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for __size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))  # Output: <class '__main__.Square'>
    print(mysquare.__dict__)  # Output: {'_Square__size': 3}

    mysquare = Square(89)
    print(type(mysquare))  # Output: <class '__main__.Square'>
    print(mysquare.__dict__)  # Output: {'_Square__size': 89}

    mysquare = Square()
    print(type(mysquare))  # Output: <class '__main__.Square'>
    print(mysquare.__dict__)  # Output: {'_Square__size': 0}

    try:
        mysquare = Square("3")
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)  # Output: size must be an integer

    try:
        mysquare = Square(3.14)
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)  # Output: size must be an integer

    try:
        mysquare = Square(-89)
        print(type(mysquare))
        print(mysquare.__dict__)
    except Exception as e:
        print(e)  # Output: size must be >= 0
