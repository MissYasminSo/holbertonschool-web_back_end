#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of floats representing the time delays"""
    task_wait_random = __import__('3-tasks').task_wait_random

    results = []

    tasks = [task_wait_random(max_delay) for i in range(n)]
    for future in asyncio.as_completed(tasks):
        result = await future
        results.append(result)

    return results
