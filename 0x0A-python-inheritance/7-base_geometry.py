#!/usr/bin/python3
"""Defines a BaseGeometry class representing base geometry."""


class BaseGeometry:
    """Represent base geometry.

    Methods:
        area: Returns the area of the geometry.
        integer_validator: Validates a parameter as an integer.
    """

    def area(self):
        """Raises an exception indicating that the method is not implemented.

        Raises:
            NotImplementedError: Always raised.
        """
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If the parameter is not an integer.
            ValueError: If the parameter is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
