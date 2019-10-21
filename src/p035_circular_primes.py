"""
Problem 35: Circular primes
http://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from typing import Iterable

from src.common.primes import get_primes_set


def _get_circular_numbers(number: int) -> Iterable[int]:
    """Get all circular numbers for a given number `number`.

    Example:
    1234 -> 1234, 2341, 3412, 4123
    """
    number_str = str(number)
    for idx in range(len(number_str)):
        yield int(number_str[idx:] + number_str[:idx])


def _get_circular_primes(threshold: int) -> Iterable[int]:
    """Get all circular primes up to a threshold `threshold`."""
    primes = get_primes_set(threshold)
    for prime in primes:
        is_circular_prime = True
        for circular_number in _get_circular_numbers(prime):
            if circular_number not in primes:
                is_circular_prime = False
                break
        if is_circular_prime:
            yield prime


def main() -> None:
    """Main function."""
    threshold = int(1e6)
    print(f'There are {len(list(_get_circular_primes(threshold))):,} circular primes ' \
          f'below {threshold:,}.')


if __name__ == '__main__':
    main()
