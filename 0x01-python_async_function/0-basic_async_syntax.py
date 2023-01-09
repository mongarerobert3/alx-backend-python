#!/usr/bin/env python3
"""asynchronous coroutine"""
import random


async def wait_random(max_delay: int = 10):
    """asynchronous coroutine"""
    await(0, max_delay)
