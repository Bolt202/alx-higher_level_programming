#!/usr/bin/python3
"""Defines a function for adding attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute is added.
        att (str): The name of the attribute.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Unable to add new attribute")
    setattr(obj, att, value)
