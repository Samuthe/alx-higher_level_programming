#!/usr/bin/python3

def remove_char_at(str, n):
    if n >= 0:
        x = str[:n] + str[n + 1:]
        return x
    else:
        return str
