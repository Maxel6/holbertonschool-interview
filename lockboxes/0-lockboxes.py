#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of list of int): A list of lists where
    each sublist contains keys
                                 for other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """
    # Set to track which boxes have been opened
    opened = set()

    # List to store the keys we find, starting with the key to the first box
    keys = [0]

    # Loop while there are keys to try
    while keys:
        key = keys.pop()  # Remove a key from the list

        if key not in opened:  # If the corresponding box is not yet opened
            opened.add(key)  # Mark the box as opened

            # Add the keys found in this box to the list of keys to try
            keys.extend(boxes[key])

    # Return True if all boxes are opened, otherwise False
    return len(opened) == len(boxes)
