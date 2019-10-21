"""
Prime number utility functions.
"""

from typing import Iterator, Dict, Set
import math


def get_prime_factors(number: int) -> Iterator[int]:
    """Get prime factors of a given number `number` as generator."""
    if number < 0:
        raise ValueError('Negative numbers are not supported.')

    i = 2
    while i <= math.floor(math.sqrt(number)):
        if number % i == 0:
            yield i
            number //= i
            i = 2
        else:
            i += 1
    yield number


def get_prime_factors_map(number: int) -> Dict[int, int]:
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
    for prime in get_prime_factors(number):
        prime_factors_map[prime] = prime_factors_map.get(prime, 0) + 1
    return prime_factors_map


def is_prime(number: int) -> bool:
    """Check if the given number `number` is a prime number."""
    try:
        prime_factors = get_prime_factors(number)
        return next(prime_factors) == number
    except ValueError:
        return False


def get_primes_set(threshold: int) -> Set:
    """Get all prime numbers up to a threshold `threshold` as set."""
    return {number for number in range(2, threshold) if is_prime(number)}
