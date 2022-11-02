#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(sys.argv[1], data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        this = response.read()
        print(this.decode("utf-8"))
