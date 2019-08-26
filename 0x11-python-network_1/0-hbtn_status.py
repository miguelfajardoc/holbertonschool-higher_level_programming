#!/usr/bin/python3

if __name__ == "__main__":
    from urllib import request

    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
