#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio
import concurrent.futures


async def wait_n(n: int, max_delay: int) -> float:
    """Returns a list of floats representing the time delays"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    results = []

    tasks = [wait_random(max_delay) for i in range(n)]
    for future in asyncio.as_completed(tasks):
        result = await future
        results.append(result)

    return results
