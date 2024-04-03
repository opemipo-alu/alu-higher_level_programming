#!/usr/bin/python3


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with the given size.
        Args:
            size (int): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("{}".format(my_square_1.area()))  # Correct output: 9

    my_square_2 = Square(89)
    print("{}".format(my_square_2.area()))  # Correct output: 7921

    my_square_3 = Square()
    print("{}".format(my_square_3.area()))  # Correct output: 0


