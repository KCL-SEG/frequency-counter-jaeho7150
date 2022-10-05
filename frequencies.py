"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

# Return a dictionary mapping items to their frequencies
def frequencies(items):
    frequencies = {}

    # Iterate through all items
    for item in items:
        # convert item into strings
        itemStr = str(item)
        # Increment count of each item by 1
        if itemStr in frequencies:
            frequencies[itemStr] += 1
        # If there was no item, set the count as 1
        else:
            frequencies[itemStr] = 1
    # Return the dictionary
    return frequencies
