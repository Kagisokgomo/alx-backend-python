#!/usr/bin/env python3
"""
This module contains a function that returns an asyncio.Task for wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
