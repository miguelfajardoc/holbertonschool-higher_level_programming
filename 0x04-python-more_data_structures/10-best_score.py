#!/usr/bin/python3
def best_score(a_dictionary):
    maximo = -10000000000
    if not a_dictionary:
        return None
    for name, score in a_dictionary.items():
        if maximo < score:
            man = name
            maximo = score
    return man
