#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers
    Args:
        list_of_integers: List of integers to search for a peak
    Returns:
        The peak value found in the list
    """
    if not list_of_integers:
        return None
    peak = max(list_of_integers)
    return peak
