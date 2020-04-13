#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the
 X-Request-Id variable found in the header of the response
"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv
    req = urllib.request.Request(argv[1])

    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
