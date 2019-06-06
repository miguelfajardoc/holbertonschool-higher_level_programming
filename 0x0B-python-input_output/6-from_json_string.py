#!/usr/bin/python3
"""JSON string"""
import json


def from_json_string(my_str):
    """function that convert an json string to an object"""

    return json.loads(my_str)
