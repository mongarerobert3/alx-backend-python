#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
