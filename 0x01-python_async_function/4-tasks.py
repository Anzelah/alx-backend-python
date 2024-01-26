#!/usr/bin/env python3
"""Spawning another function"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asychronous functi that spawns wait_random n times"""
    res = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*res)
    return sorted(delays)
