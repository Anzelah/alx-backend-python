#!/usr/bin/env python3
"""Defines a function"""

from typing import List, Union
"""Import a module"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of floats and int"""
    return sum(mxd_lst)
