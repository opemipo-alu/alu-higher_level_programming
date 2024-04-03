#!/usr/bin/python3

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

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

if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))  # Output: <class '2-square.Square'>
    print(my_square_1.__dict__)  # Output: {'_Square__size': 3}

    my_square_2 = Square()
    print(type(my_square_2))  # Output: <class '2-square.Square'>
    print(my_square_2.__dict__)  # Output: {'_Square__size': 0}

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)  # Output: 'Square' object has no attribute 'size'

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)  # Output: 'Square' object has no attribute '__size'

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))  # Output: size must be an integer
        print(my_square_3.__dict__)  # Output: {}

    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))  # Output: size must be >= 0
        print(my_square_4.__dict__)  # Output: {}

    except Exception as e:
        print(e)

