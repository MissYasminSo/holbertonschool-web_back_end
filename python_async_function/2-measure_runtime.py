#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time delay"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
