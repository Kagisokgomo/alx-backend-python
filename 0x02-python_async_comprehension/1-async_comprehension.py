#!/usr/bin/env python3
from typing import List
from async_generator_0 import async_generator

async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension over async_generator."""
    return [number async for number in async_generator()]
