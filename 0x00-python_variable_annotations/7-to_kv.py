#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type-annotated function to_kv"""
    return (k, v * v)
