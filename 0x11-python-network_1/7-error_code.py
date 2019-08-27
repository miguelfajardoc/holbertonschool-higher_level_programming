#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get, HTTPError
    from sys import argv

    try:
        req = get(argv[1])
        req.raise_for_status()
        print(req.text)

    except:
        if req.status_code >= 400:
            print("Error code: {}".format(req.status_code))
