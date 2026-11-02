#!/usr/bin/env python3
"""Module: Practicing using coroutines"""

import asyncio
from typing import Generator


async def async_comprehension() -> Generator[float, None, None]:
    """Return a list of random numbers"""

    async_generator = __import__('0-async_generator').async_generator

    async for i in async_generator():
        yield result.append(i)
