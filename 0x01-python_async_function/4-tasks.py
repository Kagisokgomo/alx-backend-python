#!/usr/bin/env python3
"""
This module contains a function to run multiple asynchronous tasks using task_wait_random.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns a list
    of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value for task_wait_random.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
