#!/usr/bin/env python3
"""
This module contains a function that returns another function to multiply a float by a multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    
    Args:
        multiplier (float): The multiplier to use for the returned function.
    
    Returns:
        Callable[[float], float]: A function that takes a float and returns it multiplied by the multiplier.
    """
    return lambda x: x * multiplier
