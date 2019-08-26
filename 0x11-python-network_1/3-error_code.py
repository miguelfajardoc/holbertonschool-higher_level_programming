#!/usr/bin/python3

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    from urllib.error import HTTPError

    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
