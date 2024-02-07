#!/usr/bin/python3
"""Defines a function to read text files."""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
