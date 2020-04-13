#!/usr/bin/python3
"""
gets status with urllib
"""
import urllib

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as req:
        response = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(respose.decode('utf8')))
