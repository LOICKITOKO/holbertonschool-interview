#!/usr/bin/python3
"""
Determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Checks if all the boxes can be unlocked.

    :param boxes: List of lists, where each list contains keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = {0}  # Start with the first box unlocked
    keys = set(boxes[0])  # Keys found in the first box

    while keys:
        key = keys.pop()  # Take a key from the set
        if key < n and key not in opened:
            opened.add(key)  # Unlock the box
            keys.update(boxes[key])  # Add new keys from the opened box

    return len(opened) == n
