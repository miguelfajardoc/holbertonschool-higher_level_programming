#!/usr/bin/python3
"""JSON string file"""
import json


def load_from_json_file(filename):
    """function that convert an object to a json string"""
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
