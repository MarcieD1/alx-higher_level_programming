#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name: A string representing the first name.
        last_name: A string representing the last name (optional, default is empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is", full_name)


# Example usage
say_my_name("John", "Doe")
say_my_name("Alice")
