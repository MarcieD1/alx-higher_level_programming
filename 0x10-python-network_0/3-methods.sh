#!/bin/bash
# This script takes a URL and displays all HTTP methods accepted by the server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
