#!/usr/bin/env python3
"""Defining the functins"""

import asyncio
import random
"""Import modules"""


async def wait_random(max_delay=10: int) -> float:
    """Asynchronous function using random module"""
    await asyncio.sleep(0, max_delay)
    return random.uniform(0, max_delay)
