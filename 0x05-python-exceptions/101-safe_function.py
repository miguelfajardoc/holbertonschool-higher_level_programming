#!/usr/bin/python3
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError, ArithmeticError) as error:
        eprint("Exception: {}".format(error))
        return (None)
    else:
        return (result)
