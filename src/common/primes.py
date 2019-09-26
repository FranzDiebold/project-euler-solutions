"""
Prime factors utility function.
"""

from typing import Iterator, Dict
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


def get_prime_factors_map(num: int) -> Dict[int, int]:
    """Get prime factors map.

    For the input number `60`, the output should be:
    ```
    {
        2: 2,
        3: 1,
        5: 1,
    }
    ```
    """
    prime_factors_map = {}
    for prime in get_prime_factors(num):
        prime_factors_map[prime] = prime_factors_map.get(prime, 0) + 1
    return prime_factors_map


def is_prime(num: int) -> bool:
    """Check if the given number `num` is a prime number."""
    prime_factors = get_prime_factors(num)
    return next(prime_factors) == num
