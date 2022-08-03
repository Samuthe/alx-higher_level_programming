#!/usr/bin/python3
import json
"""json obj"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        return (json.dumps(my_obj), f)
