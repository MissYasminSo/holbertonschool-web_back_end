#!/usr/bin/env python3
"""Module: Practicing using coroutines"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Return a list of random numbers"""

    for index in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
