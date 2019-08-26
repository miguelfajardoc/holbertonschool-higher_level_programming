#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get

    req = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
