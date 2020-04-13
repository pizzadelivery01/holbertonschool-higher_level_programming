#!/usr/bin/python3
"""
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and
not empty, display the id and name like this: [<id>] <name>

Otherwise:
Display Not a valid JSON is the JSON is invalid
Display No result is the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        json_dict = r.json()

        if not json_dict:
            print("No result")
        else:
            print('[{}] {}'.format(json_dict['id'],
                                   json_dict['name']))
    except ValueError:
        print("Not a valid JSON")
