"""
Proper divisor utility functions.
"""

from typing import Iterable
import math


def divisors(number: int) -> Iterable[int]:
    """Get proper divisors for given number `number`.

    Example:
    220 -> [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    The numbers may be in a random order.
    """
    yield 1
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            yield i
            if i**2 < number:
                yield number // i


def get_sum_of_divisors(number: int) -> int:
    """Get sum of proper divisors of number `number`."""
    return sum(divisors(number))


def is_perferct_number(number: int) -> bool:
    """Check if a given number `number` is a perfect number.

    A perfect number is a number for which the sum of its proper divisors
    is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be
        `1 + 2 + 4 + 7 + 14 = 28`,
    which means that 28 is a perfect number.
    """
    return get_sum_of_divisors(number) == number


def is_deficient_number(number: int) -> bool:
    """Check if a given number `number` is a deficient number.

    A number n is called deficient if the sum of its proper divisors is less than n.
    """
    return get_sum_of_divisors(number) < number


def is_abundant_number(number: int) -> bool:
    """Check if a given number `number` is a abundant number.

    A number n is called abundant if the sum of its proper divisors exceeds n.
    """
    return get_sum_of_divisors(number) > number
