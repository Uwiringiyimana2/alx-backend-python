#!/usr/bin/env python3
"""typing"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Creates multiple copies of items in a tuple.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
