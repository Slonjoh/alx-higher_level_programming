#!/usr/bin/python3
"""
Uses Basic Authentication with a personal access token
to access the GitHub API and display the user ID.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    auth = (username, password)
    response = requests.get(url, auth=auth)

    try:
        json_data = response.json()
        print(json_data.get('id'))
    except ValueError:
        print(None)
