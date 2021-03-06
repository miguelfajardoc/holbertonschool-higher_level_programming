#!/usr/bin/python3
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        eprint("Exception: {}".format(error))
        return (False)
    else:
        return (True)
