#!/usr/bin/python3

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        html = response.info()
        print(html["X-Request-Id"])
