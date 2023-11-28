#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a: An integer or float.
        b: An integer or float. Defaults to 98.

    Returns:
        An integer: the addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(1.5, 2.5))
    print(add_integer("a", "b"))
