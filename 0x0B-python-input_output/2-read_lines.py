#!/usr/bin/python3
"""
print n lines
"""


def read_lines(filename="", nb_lines=0):
    """print n lines"""
    with open(filename, 'r', encoding='utf8') as f:
        total = sum(1 for line in open(filename))
        if nb_lines <= 0 or nb_lines > total:
            print(f.read(), end="")
        else:
            for line in range(0, nb_lines):
                print(f.readline(), end="")
