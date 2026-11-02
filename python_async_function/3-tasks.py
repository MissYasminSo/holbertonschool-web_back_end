#!/usr/bin/env python3
"""Module: Experimenting with Async in Python"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a task from wait_random"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
