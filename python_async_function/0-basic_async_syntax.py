#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Return a float which represents the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
