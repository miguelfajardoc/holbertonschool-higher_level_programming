#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    req = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(req.json().get("id"))
