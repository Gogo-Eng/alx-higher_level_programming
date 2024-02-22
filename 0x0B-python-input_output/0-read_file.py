#!/usr/bin/python3
"""
functions that reads a text file
"""


def read_file(filename=""):
    """
    functions that reads a text file
    Args:
        filename: filename of the file that will be read, Defaults to "".
    """
    with open(filename, 'r', encoding='UTF8') as file:
        content = file.read()
        print(content)
