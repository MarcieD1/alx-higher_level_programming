#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

# Define the URL
url = "https://alx-intranet.hbtn.io/status"

# Fetch the URL
with urllib.request.urlopen(url) as response:
    # Read the response content
    content = response.read()

    # Print the response information
    print(f"Body response:\n    - type: {type(content)}")
    print(f"    - content: {content}")
    print(f"    - utf8 content: {content.decode('utf-8')}")
