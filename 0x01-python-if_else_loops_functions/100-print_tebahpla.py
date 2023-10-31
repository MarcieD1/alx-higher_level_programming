#!/usr/bin/python3

def print_ascii_alphabet():
    """
    Prints the ASCII alphabet in reverse order,
    alternating lowercase and uppercase characters.
    """

    for i in range(122, 96, -1):
        if i % 2:
            i -= 32
        print("{:c}".format(i), end="")

print_ascii_alphabet()
