#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get, HTTPError
    from sys import argv

    try:
        req = get(argv[1])
        print(req.text)
    except HTTPError as e:
        print("Error code: {}".format(e))
