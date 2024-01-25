#!/usr/bin/env python3
"""Defines a function"""

from typing import List
"""List from the typing module annotate lists"""


def sum_list(input_list: List[float]) -> float:
    """Sum of list containing floats"""
    return sum(input_list)
