#!/usr/bin/python3
"""
gets status with urllib
"""
import urllib

with urllib.request.urlopen("https://intranet.hbtn.io/status") as req:
    response = req.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(response), response, response.decode('utf8')))
