#!/usr/bin/env python3
"""Create a coroutine"""

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """Yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
