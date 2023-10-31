#!/usr/bin/python3
"""
This prints the ASCII alphabet in lowercase, without a new line.
"""

for i in range(ord('a'), ord('z')+1):
    print(chr(i), end="")
