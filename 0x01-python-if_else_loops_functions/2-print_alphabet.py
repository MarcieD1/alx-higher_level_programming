#!/usr/bin/python3
"""
This prints the ASCII alphabet in lowercase, without a new line.
"""

for i in range(97, 123):
    print(chr(i).format(), end="")
