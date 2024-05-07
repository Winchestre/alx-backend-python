#!/usr/bin/env python3
""" Module Doc """
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """ Function Doc """
    if key in dct:
        return dct[key]
    else:
        return default
