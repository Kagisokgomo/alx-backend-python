#!/usr/bin/env python3
"""
This module contains a function that returns a list of tuples with elements and their lengths.
"""

from typing import List, Tuple, Sequence, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element and its length.
    
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (like strings or lists).
    
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
