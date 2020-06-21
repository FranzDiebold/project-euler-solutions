"""
Prime number utility functions.
"""

from typing import Iterator, Dict, List, Set
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
    if number > 1:
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
    except (ValueError, StopIteration):
        return False


def get_sorted_primes_list(threshold: int) -> List[int]:
    """Get all prime numbers up to a threshold `threshold` (exclusive) as a sorted list."""
    return [number for number in range(2, threshold) if is_prime(number)]


# pylint: disable=invalid-name
def get_sorted_n_digit_primes(n: int) -> List[int]:
    """Get all primes with `n` digits as a sorted list."""
    return [number for number in range(pow(10, n - 1), pow(10, n)) if is_prime(number)]


def get_primes_set(threshold: int) -> Set[int]:
    """Get all prime numbers up to a threshold `threshold` (exclusive) as set."""
    return set(get_sorted_primes_list(threshold))
