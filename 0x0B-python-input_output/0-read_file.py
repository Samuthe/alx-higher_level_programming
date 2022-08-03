#!/usr/bin/python3
"""A function that reads and outputs to stdout"""


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
