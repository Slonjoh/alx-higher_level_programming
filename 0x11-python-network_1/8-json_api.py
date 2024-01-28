#!/usr/bin/python3
"""
Takes in a letter, sends a POST request,
and displays the response based on JSON content.
"""


import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        js_data = response.json()
        if js_data:
            print("[{}] {}".format(js_data.get('id'), js_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
