#!/usr/bin/python3

if __name__ == "__main__":
    from requests import get, post
    from sys import argv

    datas = {'search': argv[1]}

    req = post("https://swapi.co/api/people", params=datas)
    print("Number of results: {}".format(req.json().get("count")))
    for item in req.json()["results"]:
        print(item["name"])
