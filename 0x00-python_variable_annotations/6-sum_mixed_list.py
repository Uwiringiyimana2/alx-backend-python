#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """type-annotated function sum_mixed_list"""
    return sum(mxd_lst)
