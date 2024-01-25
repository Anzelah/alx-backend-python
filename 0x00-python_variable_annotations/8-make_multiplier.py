#!/usr/bin/env python3
"""Define functions"""

from typing import Callable
"""Import modules"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function taking a float as argument, and returning a float"""
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
