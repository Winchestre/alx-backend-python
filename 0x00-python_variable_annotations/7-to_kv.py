#!/usr/bin/env python3
""" Module Doc """


def to_kv(k: str, v: int | float) -> float:
    """ Function Doc """
    value: tuple[str, int | float] = (k, v**2)
    return value
