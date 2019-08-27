#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get
    from sys import argv

    req = get(argv[1])
    print(req.headers["X-Request-Id"])
