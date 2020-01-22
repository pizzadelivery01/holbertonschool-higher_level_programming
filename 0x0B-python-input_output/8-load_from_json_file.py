#!/usr/bin/python3
import json
"""
create from json file
"""


def load_from_json_file(filename):
    """create from json file"""
    with open(filename) as f:
        new = json.load(f)
    return new
