#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

if __name__ == "__main__":
    mysquare = Square(3)
    print(type(mysquare))
    print(mysquare.__dict__)

    mysquare = Square(89)
    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        print(mysquare.size)
    except Exception as e:
        print(e)

    try:
        print(mysquare._size)
    except Exception as e:
        print(e)

