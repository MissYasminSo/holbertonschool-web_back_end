#!/usr/bin/env python3
"""Module: Practicing using coroutines"""

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """Return a list of random numbers"""

    async_generator = __import__('0-async_generator').async_generator

    result = []
    async for i in async_generator():
        result.append(i)

    return result
