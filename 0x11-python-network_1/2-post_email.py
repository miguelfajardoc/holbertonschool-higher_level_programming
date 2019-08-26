#!/usr/bin/python3

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv


    email = {'email' : argv[2]}
    email = parse.urlencode(email)
    email = email.encode('ascii')

    req = request.Request(argv[1], email)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
