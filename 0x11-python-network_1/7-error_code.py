#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
