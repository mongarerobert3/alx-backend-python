#!/usr/bin/env python3
"""coroutine called async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator () -> Generator[float, None, None]:
    '''Generates numbesr Asynchronously'''
    for i in range (10):
        await asyncio.sleep(1)
        yield random.random() * 10
