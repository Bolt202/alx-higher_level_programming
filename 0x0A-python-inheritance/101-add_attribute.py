#!/usr/bin/python3
"""Defines a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if feasible.

    Args:
        obj (any): The object to which an attribute is to be added.
        att (str): The name of the attribute to be added.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
