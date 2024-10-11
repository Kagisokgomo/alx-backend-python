#!/usr/bin/env python3
"""
This module contains a function that zooms an array based on a given factor.
"""

from typing import List, Iterable

def zoom_array(lst: Iterable[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the input array by repeating each element a specified number of times.

    Args:
        lst (Iterable[int]): The input array to zoom in on.
        factor (int): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A new list containing the zoomed-in values.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# The following line should raise a TypeError because we are passing a float instead of an int
# Uncommenting the following line will result in a type checking error with mypy.
# zoom_3x = zoom_array(array, 3.0)  # This should be changed to zoom_array(array, 3)
