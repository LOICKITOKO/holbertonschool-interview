#!/usr/bin/python3

def can_unlock_all(boxes):
    """Determine if all boxes can be opened."""
    n = len(boxes)
    opened = {0}  # Start with the first box opened
    keys = set(boxes[0])  # Start with the keys from the first box

    while keys:
        key = keys.pop()  # Take a key from the set
        if key < n and key not in opened:  # Check if it opens a new box
            opened.add(key)
            keys.update(boxes[key])  # Add new keys from the opened box

    return len(opened) == n  # If all boxes are opened, return True
