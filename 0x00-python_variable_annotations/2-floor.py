#!/usr/bin/env python3
"""type-annotated function floor"""


def floor(n: float) -> int:
    """function floor"""
    if n > 0:
        return int(n)
    else:
        if int(n) != n:
            return int(n) - 1
        return int(n)
