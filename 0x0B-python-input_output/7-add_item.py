#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list,
    and then save them to a file:
    -You must use your function save_to_json_file from
        5-save_to_json_file.py
    -You must use your function load_from_json_file from
        6-load_from_json_file.py
    -The list must be saved as a JSON representation in
        a file named add_item.json
    -If the file doesn’t exist, it should be created
    -You don’t need to manage file permissions / exceptions.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


new_list = []
old_list = []

for obj in sys.argv:
    if obj is not sys.argv[0]:
        new_list.append(obj)
try:
    old_list = load_from_json_file("add_item.json")
except ValueError:
    pass
if new_list:
    if old_list:
        new_list += old_list
    save_to_json_file(new_list, "add_item.json")
