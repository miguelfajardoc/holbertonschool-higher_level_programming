#!/usr/bin/python3

if __name__ == "__main__":
    from requests import post
    from sys import argv

    req = post(argv[1], data={'email': argv[2]})
    print(req.text)
