#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """writing into a file stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
