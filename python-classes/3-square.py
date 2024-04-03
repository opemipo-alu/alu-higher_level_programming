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
    print("Area: {}".format(my_square_1.area()))  # Output: Area: 9

    try:
        print(my_square_1.size)  # Output: AttributeError: 'Square' object has no attribute 'size'
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)  # Output: AttributeError: 'Square' object has no attribute '__size'
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
        print("Area: {}".format(my_square_2.area()))  # Output: Area: 25

