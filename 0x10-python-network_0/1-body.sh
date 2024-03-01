#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" -X GET -L -s -f -o /tmp/body | cat /tmp/body
