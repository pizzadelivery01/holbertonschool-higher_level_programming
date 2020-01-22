#!/usr/bin/python3
"""
read file and print to stdout
"""


def read_file(filename=""):
    """read file and print to stdout"""
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read()
    print("{}".format(text), end="")
