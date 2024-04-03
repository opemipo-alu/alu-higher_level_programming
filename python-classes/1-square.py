#!/usr/bin/python3

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '__main__.Square'>
    print(my_square.__dict__)  # Output: {'_Square__size': 3}

    try:
        print(my_square.size)  # Output: AttributeError: 'Square' object has no attribute 'size'
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)  # Output: AttributeError: 'Square' object has no attribute '__size'
    except Exception as e:
        print(e)

