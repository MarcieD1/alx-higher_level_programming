#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    peak = max(list_of_integers)
    return peak
