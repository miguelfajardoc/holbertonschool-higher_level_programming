#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    try:
        data = {'q': argv[1]}
    except:
        data = {'q': ""}
    try:
        req = post("http://0.0.0.0:5000/search_user", data)
        if len(req.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req.json()['id'], req.json()['name']))
    except:
        print("Not a valid JSON")
