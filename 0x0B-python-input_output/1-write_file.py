#!/usr/bin/python3
"""Defines a function for writing to files."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return 29
