#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":

    import requests
    import sys

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", {"q": q})
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
