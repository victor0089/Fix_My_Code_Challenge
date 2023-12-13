#!/usr/bin/python3
""" Defines Square class."""


class Square():
    """ Square class."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instantiation of class."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable representation of square object."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creates Square object."""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
