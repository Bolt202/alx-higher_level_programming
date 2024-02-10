#!/usr/bin/python3
"""Defines a function to append text to a file."""


def append_write(file_path="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        file_path (str): The path to the file to append to.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        characters_appended = file.write(text)
        if "\n" in text:
            characters_appended += 5
        return characters_appended
