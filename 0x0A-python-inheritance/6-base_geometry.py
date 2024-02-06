#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base class for representing base geometry."""

    def area(self):
        """Raises an exception indicating that the method is not implemented.

        Raises:
            NotImplementedError: Always raised.
        """
        raise NotImplementedError("area() is not implemented")
