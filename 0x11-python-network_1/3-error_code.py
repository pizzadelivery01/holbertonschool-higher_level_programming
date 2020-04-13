#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request
 to the URL and displays the body of the response
 and handle httpError
"""
from urllib import error, request, parse

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
