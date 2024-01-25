#!/usr/bin/env python3
"""Defines the function"""

from typing import Union, Tuple
"""Import modulesto use"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return a string and float"""
    return (k, v * v)
