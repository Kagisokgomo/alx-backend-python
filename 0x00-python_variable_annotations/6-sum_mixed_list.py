#!/usr/bin/env python3
"""
This module contains a function to sum a list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing both integers and floats.
    
    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.
    
    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(mxd_lst)
