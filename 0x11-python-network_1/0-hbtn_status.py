#!/usr/bin/python3
"""
gets status with urllib
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    import urllib.request

    response = Request('https://intranet.hbtn.io/status')
    with urlopen(response) as req:
        html = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
