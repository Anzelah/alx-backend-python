#!/usr/bin/env python3
"""Defines modules"""


from typing import Sequence, Iterable, Tuple, List
"""Import modules"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Appropriately annotate this function"""
    return [(i, len(i)) for i in lst]
