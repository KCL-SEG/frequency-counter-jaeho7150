"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for item in items:
        if item in frequencies:
            frequencies[str(item)] += 1
        else:
            frequencies[str(item)] = 1
    return frequencies
