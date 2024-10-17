#!/usr/bin/env python3
import asyncio
import time
from typing import List
from async_comprehension_1 import async_comprehension

async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension four times in parallel."""
    start_time = time.perf_counter()  # Start the timer
    await asyncio.gather(async_comprehension(), 
                         async_comprehension(), 
                         async_comprehension(), 
                         async_comprehension())
    end_time = time.perf_counter()  # End the timer
    return end_time - start_time  # Return the elapsed time
