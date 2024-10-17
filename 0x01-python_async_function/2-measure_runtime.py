#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of wait_n.
"""

import time
import asyncio
from typing import List
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per wait.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        float: The average time per call to wait_random.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    
    return total_time / n
