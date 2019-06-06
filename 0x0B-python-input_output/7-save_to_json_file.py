#!/usr/bin/python3
"""JSON string file"""
import json


def save_to_json_file(my_obj, filename):
    """function that convert an object to a json string"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
