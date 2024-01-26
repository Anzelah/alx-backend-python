#!/usr/bin/env python3
"""Defining the functins"""

import asyncio
import random
"""Import modules"""


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function using random module"""
    await asyncio.sleep(0, max_delay)
    return random.uniform(0, max_delay)
