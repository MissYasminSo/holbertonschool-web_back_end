#!/usr/bin/env python3
"""Module: Practicing using coroutines"""

import asyncio
import time


async def measure_runtime() -> float:
    """Return float that represents the runtime"""

    async_comprehension = __import__('1-async_comprehension').async_comprehension

    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()

    return end - start
