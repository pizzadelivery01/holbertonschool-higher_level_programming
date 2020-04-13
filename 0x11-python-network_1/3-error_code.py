#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request
 to the URL and displays the body of the response
 and handle httpError
"""
from urllib import error as error
from urllib import request as request

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
