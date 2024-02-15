#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: a string of characters

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        i = 0
        while i < len(text):
            print(text[i], end='')
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print('\n')
                if i == len(text) - 1:
                    break
                if text[i + 1] == ' ':
                    i += 1
                while text[i] == ' ' and text[i+1] == ' ' and i+1 < len(text):
                    i += 1
            i += 1
