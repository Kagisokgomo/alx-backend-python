#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a value from a dictionary.
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')  # Declare a type variable

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Union[T, None]:
    """
    Retrieves the value associated with a key from a dictionary safely.
    
    Args:
        dct (Mapping[Any, T]): A mapping (like a dictionary) from which to retrieve the value.
        key (Any): The key whose associated value is to be retrieved.
        default (Optional[T]): The value to return if the key is not found. Defaults to None.
    
    Returns:
        Union[T, None]: The value associated with the key if it exists; otherwise, returns default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
