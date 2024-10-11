#!/usr/bin/env python3
"""
This module contains a function to return a tuple where the first element is a string and
the second element is the square of a number (int or float) as a float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string and the second element
    is the square of the given int or float.
    
    Args:
        k (str): A string key.
        v (Union[int, float]): A number (int or float) to square.
    
    Returns:
        Tuple[str, float]: A tuple with the string and the square of the number as a float.
    """
    return (k, float(v ** 2))
