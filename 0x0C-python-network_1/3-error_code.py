#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":

    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(
                urllib.request.Request(sys.argv[1])
        ) as response:
            this = response.read()
            print(this.decode("utf-8"))
    except urllib.error.HTTPError as e:
        error = ''.join((item for item in str(e) if item.isdigit()))
        print("Error code:", error)
