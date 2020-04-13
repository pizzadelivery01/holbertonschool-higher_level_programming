#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request
 to the URL and displays the body of the response
 and handle httpError
"""

if __name__ == "__main__":
    import urllib.error
    import urllib.request
    from sys import argv
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except ullib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
