#!/usr/bin/python3
"""
adds all arguments to a Python list
"""


import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load("add_item.json")
except:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save(my_list, "add_item.json")
