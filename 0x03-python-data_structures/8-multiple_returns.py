#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        f = None
    else:
        f = sentence[0]
    tup = len(sentence), f
    return(tup)
