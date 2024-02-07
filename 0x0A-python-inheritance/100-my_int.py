#!/usr/bin/python3
"""Defines a class MyInt which inherits from int."""


class MyInt(int):
    """Reverses the behavior of == and != operators."""

    def __eq__(self, value):
        """Overrides == operator to behave like !=."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator to behave like ==."""
        return self.real == value
