#!/usr/bin/env python3
"""Asynchronous comprehension"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use async cmrehension to return random numbers"""
    return [i async for i in async_generator()]
