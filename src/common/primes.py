"""
Prime factors utility function.
"""

from typing import Iterator
import math


def get_prime_factors(num: int) -> Iterator[int]:
    """Get prime factors of a given number `num` as generator."""
    i = 2
    while i <= math.floor(math.sqrt(num)):
        if num % i == 0:
            yield i
            num //= i
            i = 2
        else:
            i += 1
    yield num


def is_prime(num: int) -> bool:
    """Check if the given number `num` is a prime number."""
    prime_factors = get_prime_factors(num)
    return next(prime_factors) == num
