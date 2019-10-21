"""
Problem 37: Truncatable primes
http://projecteuler.net/problem=37

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are
both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from typing import Iterable

from src.common.primes import get_primes_set


def _get_truncated_numbers(number: int) -> Iterable[int]:
    """Get all truncated numbers for a given number `number`.

    Example:
    1234 -> 1234, 123, 12, 1, 234, 34, 4
    """
    number_str = str(number)
    yield number
    for idx in range(1, len(number_str)):
        yield int(number_str[idx:])
        yield int(number_str[:idx])


def _get_truncatable_primes(threshold: int) -> Iterable[int]:
    """Get all truncatable primes up to a threshold `threshold`."""
    primes = get_primes_set(threshold)
    for prime in primes:
        if prime < 10:
            continue

        is_truncatable_prime = True
        for truncated_number in _get_truncated_numbers(prime):
            if truncated_number not in primes:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            yield prime


def main() -> None:
    """Main function."""
    threshold = int(1e6)
    truncatable_primes = list(_get_truncatable_primes(threshold))
    print(f'The sum of all primes {len(truncatable_primes):,} that are both truncatable from ' \
          f'left to right and right to left is {sum(truncatable_primes):,}.')


if __name__ == '__main__':
    main()
