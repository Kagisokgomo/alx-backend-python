#!/usr/bin/env python3
import asyncio
import random

async def async_generator() -> float:
    """Asynchronously generates 10 random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
