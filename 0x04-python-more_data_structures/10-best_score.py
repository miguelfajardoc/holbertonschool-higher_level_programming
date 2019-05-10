#!/usr/bin/python3
def best_score(a_dictionary):
    maximo = -10000000
    if a_dictionary is None:
        return None
    for name, score in a_dictionary.items():
        if maximo < score:
            man = name
            maximo = score
    return man
