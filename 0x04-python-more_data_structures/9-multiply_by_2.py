#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for name, age in a_dictionary.items():
        new[name] = age * 2
    return new
