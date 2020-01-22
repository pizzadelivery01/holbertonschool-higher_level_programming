#!/usr/bin/python3
"""
adds all arguments to a Python list
"""


import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

new = "add_item.json"

try:
    my_list = load(new)
    save(my_list + argv[1:], new)
except:
    save([] + argv[1:], new)
