#!/usr/bin/env python3
"""
This module contains a function to perform an asynchronous wait.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): Maximum number of seconds to wait. Default is 10.

    Returns:
        float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
