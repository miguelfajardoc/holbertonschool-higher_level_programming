#!/usr/bin/python3
"""JSON string file load and save"""
from pathlib import Path
from sys import argv


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
my_list = []
i = 1
jeison = Path("add_item.json")

if jeison.is_file():
    my_list = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    my_list += [argv[i]]

save_to_json_file(my_list, "add_item.json")
