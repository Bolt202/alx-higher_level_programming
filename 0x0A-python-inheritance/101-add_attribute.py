#!/usr/bin/python3
"""Defines a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if feasible.

    Args:
        obj (any): The object to which an attribute is added.
        att (str): The name of the attribute.
        value (any): The value assigned to the attribute.
    Raises:
        TypeError: If the attribute addition is not possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cannot add new attribute")
    setattr(obj, att, value)
