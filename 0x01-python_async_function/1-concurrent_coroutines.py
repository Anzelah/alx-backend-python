#!/usr/bin/env python3
"""Spawning another function"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asychronous functi that spawns wait_random n times"""
    res = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*res)
    return sorted(delays)
