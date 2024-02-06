#!/usr/bin/python3
"""Defines a function that checks if an object is an inherited instance of a class."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class or any of its subclasses.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is an instance of a_class or any of its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
