#!/usr/bin/python3

def max_integer(lst):
    """
    Returns the maximum integer from a list of integers.

    Args:
        lst: A list of integers.

    Returns:
        The maximum integer in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the list contains non-integer values.
    """
    if not lst:
        raise ValueError("List is empty")

    if not all(isinstance(x, int) for x in lst):
        raise TypeError("List contains non-integer values")

    return max(lst)
