#!/bin/bash
# This script sends a GET request to a URL with a specific header and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
