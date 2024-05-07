#!/usr/bin/env python3
""" Module Doc """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function Doc """

    def inner_multiplier(recursor: float) -> float:
        """ Function Doc """
        return recursor * multiplier

    return inner_multiplier
