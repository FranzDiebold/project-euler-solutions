"""
Special numbers utility functions.
"""
# pylint: disable=invalid-name

import math


def is_triangle_number(number: int) -> bool:
    """Check if a given number `number` is a triangle number of the form 1/2 * n * (n+1)."""
    return ((math.sqrt(8*number + 1) - 1) / 2.0).is_integer()


def get_pentagonal_number(n: int) -> int:
    """Get Pentagonal number `P_n=n*(3n−1)/2` for a given number `n`."""
    return (n * (3*n - 1)) // 2


def is_pentagonal_number(number: int) -> bool:
    """Check if a given number `number` is a pentagonal number of the form n * (3*n − 1) / 2."""
    return ((math.sqrt(24*number + 1) + 1) / 6.0).is_integer()


def get_hexagonal_number(n: int) -> int:
    """Get Hexagonal number `H_n=n*(2n−1)` for a given number `n`."""
    return n * (2*n - 1)


def is_hexagonal_number(number: int) -> bool:
    """Check if a given number `number` is a hexagonal number of the form n * (2*n − 1)."""
    return ((math.sqrt(8*number + 1) + 1) / 4.0).is_integer()
