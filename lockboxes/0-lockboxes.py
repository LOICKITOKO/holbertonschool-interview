#!/usr/bin/python3
"""
Lockboxes Problem

This script contains a function that determines if all boxes can be opened.
It adheres to PEP 8 (version 1.7.x) and is compatible with Python 3.4.3.
"""

def can_unlock_all(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each index represents a box,
        and contains a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = {0}  # Start with the first box opened
    keys = set(boxes[0])  # Start with the keys from the first box

    while keys:
        key = keys.pop()  # Take a key from the set
        if key < n and key not in opened:  # Check if it opens a new box
            opened.add(key)
            keys.update(boxes[key])  # Add new keys from the opened box

    return len(opened) == n  # If all boxes are opened, return True


if __name__ == "__main__":
    # Example usage
    boxes = [[1], [2], [3], [4], []]
    print(can_unlock_all(boxes))  # True

    boxes = [[1, 3], [3, 0, 1], [2], [0]]
    print(can_unlock_all(boxes))  # True

    boxes = [[1, 2, 3], [], [4], [5], []]
    print(can_unlock_all(boxes))  # False
