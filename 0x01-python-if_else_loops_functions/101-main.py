#!/usr/bin/python3

def remove_char_at(string, n):
    """
    Creates a copy of the string, removing the character at the position n.
    """
    return string[:n] + string[n+1:]

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
