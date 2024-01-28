#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body of the response.
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""


from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
