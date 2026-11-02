#!/usr/bin/env python3
"""Module: Practicing using coroutines"""

import asyncio
import random


async def async_generator():
    """Return a list of random numbers"""

    for index in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
