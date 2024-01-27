#!/usr/bin/env python3
"""Create a coroutine"""
import asyncio
import random


async def async_generator() -> float:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)